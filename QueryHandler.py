from google.cloud import bigquery
client = bigquery.Client()
import geopandas as gpd
import pandas as pd
from datetime import datetime
from datetime import timedelta


def CountyNum(state_of_interest):
    # Read shapefile containing county geometry
    usa = gpd.read_file('C:/djangosite/djangosite/coviddashboard/2020_counties/cb_2020_us_county_500k.shp')
    # Create dataframe for specified state
    df = usa.loc[usa['STUSPS'] == state_of_interest].sort_values(by='GEOID', ascending=True).reset_index(drop=True)
    num_counties = len(df)
    return num_counties


def BuildQueryEU(query_type, query_param, query_country, query_region=None, query_date=None):
    # Latest = ~3 days from current date due to slow data filling
    lag = timedelta(days=3)
    now = datetime.now()-lag
    latest = now.strftime('%Y-%m-%d')

    if query_date is None:       
        if query_type == 'country':
            sql = f"""
                SELECT distinct location_key, iso_3166_1_alpha_3, {query_param}, date FROM `bigquery-public-data.covid19_open_data_eu.covid19_open_data`
                WHERE location_key like '__' and iso_3166_1_alpha_3 = '{query_country}' AND {query_param} IS NOT NULL AND date = '{latest}'
                ORDER BY date DESC
                limit 1
                """

        elif query_type == 'region':
            sql = f"""
                SELECT DISTINCT location_key, iso_3166_1_alpha_3, {query_param}, date FROM `bigquery-public-data.covid19_open_data_eu.covid19_open_data`
                WHERE location_key like '__' and iso_3166_1_alpha_3 in {str(query_region).replace('[','(').replace(']',')')} AND {query_param} IS NOT NULL AND date = '{latest}'
                ORDER BY date DESC
                LIMIT {len(query_region)}
                """

    else:
        if query_type == 'country':
            sql = f"""
                SELECT distinct location_key, iso_3166_1_alpha_3, {query_param}, date FROM `bigquery-public-data.covid19_open_data_eu.covid19_open_data`
                WHERE location_key like '__' and iso_3166_1_alpha_3 = '{query_country}' AND {query_param} IS NOT NULL AND date = '{latest}'
                ORDER BY date DESC
                limit 1
                """

        elif query_type == 'region':
            sql = f"""
                SELECT DISTINCT location_key, iso_3166_1_alpha_3, {query_param}, date FROM `bigquery-public-data.covid19_open_data_eu.covid19_open_data`
                WHERE location_key like '__' and iso_3166_1_alpha_3 in {str(query_region).replace('[','(').replace(']',')')} AND {query_param} IS NOT NULL AND date = '{latest}'
                ORDER BY date DESC
                LIMIT {len(query_region)}
                """

    return client.query(sql).to_dataframe().sort_values(by='iso_3166_1_alpha_3', ascending=True).reset_index(drop=True)


def BuildQueryUS(query_type, query_param, query_state=None, query_region=None, query_date=None):
    if query_date is None:       
        if query_type == 'county':
            num_counties = CountyNum(query_state)
            # County by Latest Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key LIKE 'US_{query_state}______' AND {query_param} IS NOT NULL
                ORDER BY date DESC
                LIMIT {num_counties}
                """

        elif query_type == 'state':
            # State by Latest Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key = 'US_{query_state}' AND {query_param} IS NOT NULL
                ORDER BY date DESC
                LIMIT 1
                """

        elif query_type == 'region':
            # Region by Latest Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key in {str(query_region).replace('[','(').replace(']',')')} AND {query_param} IS NOT NULL
                ORDER BY date DESC
                LIMIT {int(len(query_region)/9)}
                """

        else:
            # Country by Latest Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key LIKE 'US___' AND {query_param} IS NOT NULL and location_key NOT IN ('US_GU', 'US_PR', 'US_VI', 'US_MP', 'US_AS')
                ORDER BY date DESC
                LIMIT 51
                """
    else:
        if query_type == 'county':
            num_counties = CountyNum(query_state)
            # County on Specific Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key LIKE 'US_{query_state}______' AND {query_param} IS NOT NULL AND date = '{query_date}'
                ORDER BY date DESC
                LIMIT {num_counties}
                """

        elif query_type == 'state':
            # State on Specific Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key = 'US_{query_state}' AND {query_param} IS NOT NULL AND date = '{query_date}'
                ORDER BY date DESC
                LIMIT 1
                """

        elif query_type == 'region':
            # Region by Latest Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key in {str(query_region).replace('[','(').replace(']',')')} AND {query_param} IS NOT NULL AND date= '{query_date}'
                ORDER BY date DESC
                LIMIT {int(len(query_region)/9)}
                """
        else:
            # Country on Specific Date
            sql = f"""
                SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                WHERE location_key LIKE 'US___' AND {query_param} IS NOT NULL and location_key NOT IN ('US_GU', 'US_PR', 'US_VI', 'US_MP', 'US_AS') AND date = '{query_date}'
                ORDER BY date DESC
                LIMIT 51
                """

    return client.query(sql).to_dataframe().sort_values(by='location_key', ascending=True).reset_index(drop=True)


def MovingAverageQuery(query_type, query_param, query_state=None, start_date=None, end_date=None):
    if start_date is None:
        start_date = '2020-01-01'
    if end_date is None:
        end_date = (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')
        
    if query_type == 'state':
        sql = f"""
            SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
            WHERE location_key = 'US_{query_state}' AND {query_param} IS NOT NULL and date between '{start_date}' and '{end_date}'
            ORDER BY date ASC
            """
        return client.query(sql).to_dataframe()
    elif query_type == 'country':
        sql = f"""
            SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
            WHERE location_key LIKE 'US___' AND {query_param} IS NOT NULL and location_key NOT IN ('US_GU', 'US_PR', 'US_VI', 'US_MP', 'US_AS') 
            and date between '{start_date}' and '{end_date}'
            ORDER BY date ASC
            """
        return client.query(sql).to_dataframe()
