# Data Visualization Examples

## County-level
```sql
sql = f"""
    SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE location_key LIKE 'US_{query_state}______' AND {query_param} IS NOT NULL
    ORDER BY date DESC
    LIMIT {num_counties}
    """
```
![alt text](https://i.imgur.com/Z5V19Zb.png)

## State-level
```sql
sql = f"""
    SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE location_key = 'US_{query_state}' AND {query_param} IS NOT NULL
    ORDER BY date DESC
    LIMIT 1
    """
```
![alt text](https://i.imgur.com/MOzpOOo.png)

## Region-level
```sql
sql = f"""
    SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE location_key in {str(query_region).replace('[','(').replace(']',')')} AND {query_param} IS NOT NULL
    ORDER BY date DESC
    LIMIT {len(query_region)}
    """
```
![alt text](https://i.imgur.com/ZhSToyF.png)

## Country-level
```sql
sql = f"""
    SELECT DISTINCT location_key, {query_param}, date FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE location_key LIKE 'US___' AND {query_param} IS NOT NULL and location_key NOT IN ('US_GU', 'US_PR', 'US_VI', 'US_MP', 'US_AS')
    ORDER BY date DESC
    LIMIT 51
    """
```
![alt text](https://i.imgur.com/Zb4cQVv.png)
