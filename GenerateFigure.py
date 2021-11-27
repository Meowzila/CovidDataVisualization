import chart_studio.plotly as py
import plotly.express as px
import plotly.io as pio
import geopandas as gpd
import pandas as pd
from datetime import datetime
from datetime import timedelta


us_pop_dict = {
'US_AK': 738432,'US_AL': 4858979,'US_AR': 2978204,'US_AZ': 6828065,'US_CA': 39144818,
'US_CO': 5456574,'US_CT': 3590886,'US_DC': 705749,'US_DE': 945934,'US_FL': 20271272,
'US_GA': 10214860,'US_HI': 1431603,'US_IA': 3046355,'US_ID': 1654930,'US_IL': 12859995,
'US_IN': 6619680,'US_KS': 2911641,'US_KY': 4425092,'US_LA': 4533372,'US_MA': 6794422,
'US_MD': 6045680,'US_ME': 1328361,'US_MI': 9922576,'US_MN': 5489594,'US_MO': 6083672,
'US_MS': 2992333,'US_MT': 1032949,'US_NC': 10042802,'US_ND': 756927,'US_NE': 1896190,
'US_NH': 1330608,'US_NJ': 8958013,'US_NM': 2085109,'US_NV': 2890845,'US_NY': 19795791,
'US_OH': 11613423,'US_OK': 3911338,'US_OR': 4028977,'US_PA': 12802503,'US_RI': 1056298,
'US_SC': 4896146,'US_SD': 858469,'US_TN': 6600299,'US_TX': 27469114,'US_UT': 2763885,
'US_VA': 8382993,'US_VT': 626042,'US_WA': 7170351,'US_WI': 5771337,'US_WV': 1844128,
'US_WY': 586107}


global_pop_dict = {'AND': 77265,'ARE': 9890400,'AFG': 38928341,'ATG': 97928,'AIA': 15002,'ALB': 2862427,'ARM': 2963234,'AGO': 32866267,'ATA': 4400,'ARG': 44938712,'ASM': 55196,'AUT': 8858775,
'AUS': 25499881,'ABW': 106766,'AZE': 10139175,'BIH': 3280815,'BRB': 287371,'BGD': 164689383,'BEL': 11455519,'BFA': 20903278,'BGR': 7000039,'BHR': 1701582,'BDI': 11890781,
'BEN': 12123198,'BMU': 62273,'BRN': 437483,'BOL': 11673028,'BES': 26221,'BRA': 212559409,'BHS': 393248,'BTN': 771612,'BWA': 2351625,'BLR': 9449321,'BLZ': 397621,'CAN': 37742157,
'CCK': 596,'COD': 89561404,'CAF': 4829764,'COG': 5518092,'CHE': 8544527,'CIV': 26378275,'COK': 17564,'CHL': 17574003,'CMR': 26545863,'CHN': 1439323774,'COL': 50882884,
'CRI': 5094114,'CUB': 11326616,'CPV': 555988,'CUW': 164100,'CXR': 1843,'CYP': 875899,'CZE': 10649800,'DEU': 83019213,'DJI': 988002,'DNK': 5806081,'DMA': 71991,'DOM': 10847903,
'DZA': 43851043,'ECU': 17643060,'EST': 1324820,'EGY': 102334403,'ESH': 597330,'ERI': 3546427,'ESP': 46937060,'ETH': 114963583,'FIN': 5517919,'FJI': 896444,'FLK': 3483,
'FSM': 115021,'FRO': 48865,'FRA': 67012883,'GAB': 2225728,'GBR': 66647112,'GRD': 112518,'GEO': 3989175,'GUF': 298682,'GGY': 63276,'GHA': 31072945,'GIB': 33691,'GRL': 56772,
'GMB': 2416663,'GIN': 13132792,'GNQ': 1402985,'GRC': 10724599,'SGS': 30,'GTM': 17915567,'GUM': 168783,'GNB': 1967997,'GUY': 786559,'HKG': 7496988,'HND': 9904608,'HRV': 4076246,
'HTI': 11402533,'HUN': 9772756,'IDN': 273523621,'IRL': 4904240,'ISR': 8655541,'IMN': 85032,'IND': 1380004385,'IOT': 4000,'IRQ': 40222503,'IRN': 83992953,'ISL': 356991,
'ITA': 60359546,'JEY': 105500,'JAM': 2961160,'JOR': 10203140,'JPN': 126476458,'KEN': 53771300,'KGZ': 6524191,'KHM': 16718971,'KIR': 119446,'COM': 869595,'KNA': 53192,
'PRK': 25778815,'KOR': 51269183,'KWT': 4270563,'CYM': 65720,'KAZ': 18776707,'LAO': 7275556,'LBN': 6825441,'LCA': 183629,'LIE': 38378,'LKA': 21413250,'LBR': 5057677,'LSO': 2142252,
'LTU': 2794184,'LUX': 613894,'LVA': 1919968,'LBY': 6871286,'MAR': 36910558,'MCO': 39244,'MDA': 4033962,'MNE': 622182,'MDG': 27691019,'MHL': 59193,'MKD': 2077132,'MLI': 20250834,
'MMR': 54409794,'MNG': 3278292,'MAC': 649342,'MNP': 57556,'MTQ': 375265,'MRT': 4649660,'MSR': 4999,'MLT': 493559,'MUS': 1271767,'MDV': 540541,'MWI': 19129955,'MEX': 110991953,
'MYS': 32365998,'MOZ': 31255435,'NAM': 2540916,'NCL': 285491,'NER': 24206636,'NFK': 1748,'NGA': 206139587,'NIC': 6624554,'NLD': 17282163,'NOR': 5328212,'NPL': 29136807,
'NRU': 10834,'NIU': 1618,'NZL': 4822233,'OMN': 5106622,'PAN': 4314768,'PER': 29381884,'PYF': 280904,'PNG': 8947027,'PHL': 100979303,'PAK': 220892331,'POL': 37972812,'PCN': 50,
'PRI': 2860840,'PSE': 5101416,'PRT': 10276617,'PLW': 18092,'PRY': 7132530,'QAT': 2881060,'REU': 895308,'ROU': 19414458,'SRB': 6963764,'RUS': 145934460,'RWA': 12952208,
'SAU': 34813867,'SLB': 686878,'SYC': 98340,'SDN': 43849269,'SWE': 10230185,'SGP': 5850343,'SHN': 6071,'SVN': 2080908,'SVK': 5450421,'SLE': 7976985,'SMR': 33938,'SEN': 16743930,
'SOM': 15893219,'SUR': 586634,'SSD': 11193729,'STP': 219160,'SLV': 6486201,'SXM': 42882,'SYR': 17500657,'SWZ': 1160164,'TCA': 38718,'TCD': 16425859,'ATF': 196,'TGO': 8278736,
'THA': 69799978,'TJK': 9537642,'TKL': 1350,'TLS': 1318442,'TKM': 6031187,'TUN': 11818618,'TON': 105697,'TUR': 82003882,'TTO': 1399491,'TUV': 11792,'TWN': 23816775,'TZA': 59734212,
'UKR': 43733759,'UGA': 45741000,'UMI': 300,'USA': 331002647,'URY': 3473727,'UZB': 33469199,'VAT': 809,'VCT': 110947,'VEN': 28435943,'VGB': 30237,'VIR': 104422,'VNM': 97338583,
'VUT': 307150,'WLF': 11245,'WSM': 198410,'RKS': 1883018,'YEM': 29825967,'MYT': 272813,'ZAF': 59308690,'ZMB': 18383956,'ZWE': 14862927}


def NormalizationCheckEU(fig_type, fig_query, fig_param, normalized):
    if normalized is True:
        normal = ' per 100,000 people'
        if fig_type == 'country':
            fig_query[fig_param] = int((fig_query[fig_param][0]*100000)/global_pop_dict[fig_query['iso_3166_1_alpha_3'][0]])
        elif fig_type == 'region':
            for loc in range(len(fig_query)):
                fig_query[fig_param][loc] = int((fig_query[fig_param][loc]*100000)/global_pop_dict[fig_query['iso_3166_1_alpha_3'][loc]])
    else:
        normal = ''
    return normal 


def NormalizationCheckUS(fig_type, fig_query, fig_param, normalized):
    if normalized is True and fig_type != 'county':
        normal = ' per 100,000 people'
        if fig_type == 'state':
            fig_query[fig_param] = int((fig_query[fig_param][0]*100000)/us_pop_dict[fig_query['location_key'][0]])
        elif fig_type == 'region':
            for loc in range(len(fig_query)):
                fig_query[fig_param][loc] = int((fig_query[fig_param][loc]*100000)/us_pop_dict[fig_query['location_key'][loc]])
        elif fig_type == 'country':
            for loc in range(len(fig_query)):
                fig_query[fig_param][loc] = int((fig_query[fig_param][loc]*100000)/us_pop_dict[fig_query['location_key'][loc]])
    else:
        normal = ''
    return normal    


def GenerateFigureEU(fig_type, fig_query, fig_param, fig_country=None, normalized=False):
    # Check for normalization option
    normal = NormalizationCheckEU(fig_type, fig_query, fig_param, normalized)

    if fig_type == 'country':
        fig = px.choropleth(data_frame=fig_query,
                            locations=[fig_country],
                            locationmode="ISO-3",
                            color=fig_param,
                            labels={fig_param: fig_param.title().replace("_", " ")+normal},
                            width=1000,
                            height=800,
                            scope="europe",
                            title=f'{fig_param.title().replace("_", " ")} in {fig_country} on {str(fig_query["date"][0])}'+normal)
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(coloraxis_showscale=False)
        py.plot(fig, filename='eu_map_1', auto_open=False, include_plotlyjs='cdn')

    elif fig_type == 'region':
        fig = px.choropleth(data_frame=fig_query,
                            locations=[country for country in fig_query['iso_3166_1_alpha_3']],
                            locationmode="ISO-3",
                            color=fig_param,
                            color_continuous_scale=[(0, "white"), (0.75, "red"), (1, '#820000')],
                            labels={fig_param: fig_param.title().replace("_", " ")+normal},
                            width=1000,
                            height=800,
                            scope="europe",
                            title=f'{fig_param.title().replace("_", " ")} in specified region on {str(fig_query["date"][0])}'+normal)
        fig.update_geos(fitbounds="locations", visible=False)
        py.plot(fig, filename='eu_map_1', auto_open=False, include_plotlyjs='cdn')


def GenerateFigureUS(fig_type, fig_query, fig_param, fig_state=None, normalized=False):
    # Check for normalization option
    normal = NormalizationCheckUS(fig_type, fig_query, fig_param, normalized)

    if fig_type == 'county':
        # Read shapefile containing all US county geometries
        usa = gpd.read_file('C:/djangosite/djangosite/coviddashboard/2020_counties/cb_2020_us_county_500k.shp')

        # Obtain all county names, FIPS codes, and geometry
        df = usa.loc[usa['STUSPS'] == fig_state].sort_values(by='GEOID', ascending=True).reset_index(drop=True)

        # Create DataFrame for county-level data
        state_df = pd.DataFrame({
            'county': df['NAME'],
            'geoid': df['GEOID'],
            'geometry': df['geometry'],
            fig_param: fig_query[fig_param]})

        gdf = gpd.GeoDataFrame(data=state_df, geometry=state_df.geometry).set_index('county')
        fig = px.choropleth(data_frame=gdf,
                            geojson=gdf.geometry,
                            locations=gdf.index,
                            color=fig_param,
                            color_continuous_scale=[(0, "white"), (0.75, "red"), (1, '#820000')],
                            labels={fig_param: fig_param.title().replace("_", " ")},
                            projection="mercator",
                            width=1000,
                            height=800,
                            title=f'{fig_param.title().replace("_", " ")} in {fig_state} Counties on {str(fig_query["date"][0])}')
        fig.update_geos(fitbounds="locations", visible=False)
        py.plot(fig, filename='us_map_1', auto_open=False, include_plotlyjs='cdn')

    elif fig_type == 'state':
        fig = px.choropleth(data_frame=fig_query,
                            locations=[fig_state],
                            locationmode="USA-states",
                            color=fig_param,
                            labels={fig_param: fig_param.title().replace("_", " ")+normal},
                            width=1000,
                            height=800,
                            scope="usa",
                            title=f'{fig_param.title().replace("_", " ")} in {fig_state} on {str(fig_query["date"][0])}'+normal)
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(coloraxis_showscale=False)
        py.plot(fig, filename='us_map_1', auto_open=False, include_plotlyjs='cdn')

    elif fig_type == 'region':
        fig = px.choropleth(data_frame=fig_query,
                            locations=[state[-2:] for state in fig_query['location_key']],
                            locationmode="USA-states",
                            color=fig_param,
                            color_continuous_scale=[(0, "white"), (0.75, "red"), (1, '#820000')],
                            labels={fig_param: fig_param.title().replace("_", " ")+normal},
                            width=1000,
                            height=800,
                            scope="usa",
                            title=f'{fig_param.title().replace("_", " ")} in specified region on {str(fig_query["date"][0])}'+normal)
        fig.update_geos(fitbounds="locations", visible=False)
        py.plot(fig, filename='us_map_1', auto_open=False, include_plotlyjs='cdn')

    else:
        fig = px.choropleth(data_frame=fig_query,
                            locations=[state[-2:] for state in fig_query['location_key']],
                            locationmode="USA-states",
                            color=fig_param,
                            color_continuous_scale=[(0, "white"), (0.75, "red"), (1, '#820000')],
                            labels={fig_param: fig_param.title().replace("_", " ")+normal},
                            width=1000,
                            height=800,
                            scope="usa",
                            title=f'{fig_param.title().replace("_", " ")} in US on {str(fig_query["date"][0])}'+normal)
        fig.update_geos(fitbounds="locations", visible=False)
        py.plot(fig, filename='us_map_1', auto_open=False, include_plotlyjs='cdn')



def GenerateFigureMovingAverage(df, fig_type, param, state, start_date, end_date):
    if start_date is None:
        start_date = '2020-01-01'
    if end_date is None:
        end_date = (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')
    
    if fig_type == 'state':
        param_list = list(df[param])
        date_list = list(df['date'])

        moving_average = {i//7:(sum(param_list[i-7:i])//7) for i, val in enumerate(param_list) if i % 7 == 0 and i != 0}
        week = {i//7:date for i, date in enumerate(date_list) if i % 7 == 0 and i != 0}

        averaged = {i//7:'7-Day Average' for i, date in enumerate(date_list) if i % 7 == 0}
        average_df = pd.DataFrame([week, moving_average, averaged]).reset_index(drop=True).transpose()
        average_df.columns = ['date', param, 'Data']
        not_averaged = ['Daily' for date in date_list]
        notaverage_df = pd.DataFrame([date_list, param_list, not_averaged]).reset_index(drop=True).transpose()
        notaverage_df.columns = ['date', param, 'Data']

        combined_df = pd.concat([average_df, notaverage_df])

        fig = px.line(combined_df, x="date", y=param, 
                      color='Data', 
                      title=f'{param.title().replace("_", " ")} in {state} from {start_date} to {end_date}',
                      width=1000,
                      height=500,)
        py.plot(fig, filename='moving_average', auto_open=False, include_plotlyjs='cdn')
        
    elif fig_type == 'country':
        param_list = list(df[param])
        date_list = list(df['date'])

        moving_average_param = {i//357:(sum(param_list[i-357:i])//357) for i, val in enumerate(param_list) if i % 357 == 0 and i != 0}
        avg_week = {i//357:date for i, date in enumerate(date_list) if i % 357 == 0 and i != 0}

        non_avg_param = {i//51:(sum(param_list[i-51:i])//51) for i, val in enumerate(param_list) if i % 51 == 0 and i != 0}
        week = {i//51:date for i, date in enumerate(date_list) if i % 51 == 0 and i != 0}

        averaged = {i//357:'7-Day Average' for i, date in enumerate(date_list) if i % 357 == 0}
        average_df = pd.DataFrame([avg_week, moving_average_param, averaged]).reset_index(drop=True).transpose().dropna()
        average_df.columns = ['date', param, 'Data']

        not_averaged = {i//51:'Daily' for i, date in enumerate(date_list) if i % 51 == 0}
        notaverage_df = pd.DataFrame([week, non_avg_param, not_averaged]).reset_index(drop=True).transpose().dropna()
        notaverage_df.columns = ['date', param, 'Data']

        combined_df = pd.concat([average_df, notaverage_df])

        fig = px.line(combined_df, x="date", y=param, 
                      color='Data', 
                      title=f'{param.title().replace("_", " ")} in US from {start_date} to {end_date}',
                      width=1000,
                      height=500,)
        py.plot(fig, filename='moving_average', auto_open=False, include_plotlyjs='cdn')