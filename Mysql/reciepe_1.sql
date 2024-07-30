SELECT * FROM extinction.cofog_education;

SELECT * from cofog_education;

SELECT '경기도', cofog_education.* from cofog_education where sigun_gu like '경기도%';
SELECT '강원특별자치도', cofog_education.* from cofog_education where sigun_gu like '강원특별자치도%';

drop table cofog_education_city;

create table cofog_education_city
	SELECT '강원특별자치도' as city, cofog_education.* from cofog_education where sigun_gu like '강원특별자치도%';

insert into cofog_education_city
	SELECT '경기도' as city, cofog_education.* from cofog_education where sigun_gu like '경기도%';


select * from cofog_education_city;

select city, count(student_per_teacher_kin) 
	from cofog_education_city
    group by city;

select city, count(student_per_teacher_kin) 
	from cofog_education_city
    group by city;

select city, max(student_per_teacher_kin), min(student_per_teacher_kin) 
	from cofog_education_city
    group by city;

-- SUBSTRING_INDEX('THRESHOLD', '|', 2)  
select SUBSTRING_INDEX(SUBSTRING_INDEX(sigun_gu, ' ', -1), '_', 1) from cofog_education;
