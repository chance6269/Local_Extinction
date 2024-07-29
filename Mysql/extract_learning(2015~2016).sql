-- 2015년도, 2016년도 머신러닝을 위한 데이터셋 추출하기
SELECT 
    e.sigun_gu,  -- cofog_education 테이블의 sigun_gu 열 (조인 키로 사용)
    -- cofog_education 테이블의 나머지 열
    e.student_per_teacher_kin,
    e.teacher_per_student_pri,
    e.teacher_per_student_mid,
    e.teacher_per_student_high,
    e.student_per_class_kin,
    e.student_per_class_pri,
    e.student_per_class_mid,
    e.student_per_class_high,
    e.extra_curr_school,
    e.extra_curr_lifelong,
    e.student_per_extra_curr,
    e.kin_stu,
    e.pri_stu,
    -- extinct 테이블의 필요한 열
    ext.extinction_index, 
    ext.extinction_grade,
    -- cofog_health 테이블의 필요한 열
    h.general_hospital,
    h.hospital,
    h.clinic,
    h.dental_clinic,
    h.medicine_hospital,
    h.beds_per_thousandpeople,
    h.total_beds
FROM 
    cofog_education e
LEFT JOIN 
    extinct ext ON e.sigun_gu = ext.sigun_gu
LEFT JOIN 
    cofog_health h ON e.sigun_gu = h.sigun_gu
WHERE 
    e.sigun_gu LIKE '%2015%' OR e.sigun_gu LIKE '%2016%'
LIMIT 0, 2000;



