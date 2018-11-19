select fips, address_name, ori9, address_city, count(countyname)
from ori_to_fips
where address_name like '%PRECINCT 1'
and fips = 48097
group by fips,address_name, ori9, address_city
order by count desc;