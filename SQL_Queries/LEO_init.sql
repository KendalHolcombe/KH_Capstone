SELECT      vic.victim_id,
            vic.incident_id,
            vic.victim_type_id,
            ty.victim_type_name,
            vic.assignment_type_id,
            ass.assignment_type_name,
            vic.activity_type_id,
            act.activity_type_name,
            vic.age_range_low_num,
            vic.age_range_high_num,
            vic.age_id,
            age.age_name,
            vic.sex_code,
            vic.agency_data_year
            
FROM        nibrs_victim as vic
JOIN   nibrs_victim_type as ty
ON          vic.victim_type_id = ty.victim_type_id
JOIN   nibrs_age as age
ON          vic.age_id = age.age_id
JOIN   nibrs_assignment_type as ass
ON          ass.assignment_type_id = vic.assignment_type_id
JOIN   nibrs_activity_type as act
ON          act.activity_type_id = vic.activity_type_id;