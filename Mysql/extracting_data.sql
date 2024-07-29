-- 훈련 및 테스트 세트 추출
SELECT 
    e.*,  -- education 테이블의 모든 열
    ext.extinction_index, 
    ext.extinction_grade,
    h.general_hospital,
    h.hospital,
    h.clinic,
    h.dental_clinic,
    h.medicine_hospital,
    h.koreanmedical_clinic,
    h.beds_per_thousandpeople,
    h.total_beds
FROM 
    cofog_education e
LEFT JOIN 
    extinct ext ON e.sigun_gu = ext.sigun_gu
LEFT JOIN 
    cofog_health h ON e.sigun_gu = h.sigun_gu;
    
    
