select      DISTINCT yr AS YEAR,
            LTRIM(RTRIM(geography)) AS COUNTY,
            total_population AS POPULATION
            
from        census_populations

order by    LTRIM(RTRIM(geography)), yr