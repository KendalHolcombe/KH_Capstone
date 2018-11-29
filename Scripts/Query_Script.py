import pandas as pd
import psycopg2
import json


def Query_to_DF():
    '''

    Pass string query in and return a dataframe of query results

    INPUT: string
    OUTPUT: dataframe

    '''

    # Query variables
    train_query =
    '''
    SELECT      DISTINCT inc.incident_id AS INCIDENT_ID,
                date_part('year',inc.incident_date),
                vic.age_num,
                vic.sex_code AS VICTIM_SEX,
                oft.offense_name AS OFFENSE,
                oft.offense_category_name AS OFFENSE_CATEGORY,
                off.location_id AS LOCATION_ID,
                ori.countyname AS COUNTY,
                ags.population AS POPULATION,
                ags.population_group_desc AS POPULATION_DESCRIPTION,
                ags.total_officers AS OFFICERS,
                ags.total_civilians AS CIVILIANS,
                count(hosp.id) over (partition by hosp.county) AS HOSP_CNT,
                sum(hosp.beds) over (partition by hosp.county) AS BED_CNT,
                count(fire.id) over (partition by fire.county) AS FIRE_CNT


    FROM        nibrs_victim as vic
    JOIN        nibrs_offense as off
    ON          off.incident_id = vic.incident_id
    JOIN        nibrs_offense_type as oft
    ON          oft.offense_type_id = off.offense_type_id
    JOIN        nibrs_location_type as loc
    ON          off.location_id = loc.location_id
    JOIN        nibrs_incident as inc
    ON          inc.incident_id = vic.incident_id
    JOIN        cde_agencies as ags
    ON          ags.agency_id = inc.agency_id
    JOIN        ori_to_fips as ori
    ON          ori.ori9 = ags.ori
    JOIN        hospitals as hosp
    ON          hosp.county = ori.countyname
    JOIN        fire_houses as fire
    ON          fire.county = ori.countyname

    WHERE       vic.victim_type_id = 4
    AND         inc.incident_date BETWEEN '2014-01-01' AND '2016-12-31';
    '''
    test_query =
    '''
    SELECT      DISTINCT inc.incident_id AS INCIDENT_ID,
                date_part('year',inc.incident_date),
                vic.age_num,
                vic.sex_code AS VICTIM_SEX,
                oft.offense_name AS OFFENSE,
                oft.offense_category_name AS OFFENSE_CATEGORY,
                off.location_id AS LOCATION_ID,
                ori.countyname AS COUNTY,
                ags.population AS POPULATION,
                ags.population_group_desc AS POPULATION_DESCRIPTION,
                ags.total_officers AS OFFICERS,
                ags.total_civilians AS CIVILIANS,
                count(hosp.id) over (partition by hosp.county) AS HOSP_CNT,
                sum(hosp.beds) over (partition by hosp.county) AS BED_CNT,
                count(fire.id) over (partition by fire.county) AS FIRE_CNT


    FROM        nibrs_victim as vic
    JOIN        nibrs_offense as off
    ON          off.incident_id = vic.incident_id
    JOIN        nibrs_offense_type as oft
    ON          oft.offense_type_id = off.offense_type_id
    JOIN        nibrs_location_type as loc
    ON          off.location_id = loc.location_id
    JOIN        nibrs_incident as inc
    ON          inc.incident_id = vic.incident_id
    JOIN        cde_agencies as ags
    ON          ags.agency_id = inc.agency_id
    JOIN        ori_to_fips as ori
    ON          ori.ori9 = ags.ori
    JOIN        hospitals as hosp
    ON          hosp.county = ori.countyname
    JOIN        fire_houses as fire
    ON          fire.county = ori.countyname

    WHERE       vic.victim_type_id = 4
    AND         inc.incident_date > '2016-12-31';
    '''

    # Pull postgres details from config file to make connection
    with open('config.json') as f:
        conf = json.load(f)
        host = conf['host']
        database = conf['database']
        user = conf['user']
        passw = conf['passw']

    # Create postgres connection
    conn_str = "host={} dbname={} user={} password={}".format(host, database, user, passw)
    conn = psycopg2.connect(conn_str)

    # Run queries and return dataframes
    train_df = pd.read_sql(train_query, con=conn)
    test_df = pd.read_sql(test_query, con=conn)
    return train_df, test_df

# if __name__ == '__main__':
#     Query_to_DF()
