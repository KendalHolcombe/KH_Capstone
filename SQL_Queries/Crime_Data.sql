SELECT      DISTINCT inc.incident_id AS INCIDENT_ID,
            date_part('year',inc.incident_date),
            vic.age_num,
            vic.sex_code AS VICTIM_SEX,
            LTRIM(RTRIM(oft.offense_name)) AS OFFENSE,
            LTRIM(RTRIM(oft.offense_category_name)) AS OFFENSE_CATEGORY,
            off.location_id AS LOCATION_ID,
            LTRIM(RTRIM(loc.location_name)) AS LOCATION_NAME,
            LTRIM(RTRIM(ori.countyname)) AS COUNTY,
            ags.total_officers AS OFFICERS,
            ags.total_civilians AS CIVILIANS
            
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
AND         inc.incident_date BETWEEN '2010-01-01' AND '2015-12-31';