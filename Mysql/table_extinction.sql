use extinction;
CREATE TABLE extinct (
    sigun_gu VARCHAR(20),           -- 지역 이름을 나타내는 문자열 (최대 20자)
    extinction_index FLOAT(25) NOT NULL,  -- 소멸 지수 (NULL 값을 허용하지 않음)
    extinction_grade VARCHAR(3) NOT NULL  -- 소멸 등급 (최대 3자, NULL 값을 허용하지 않음)
);

CREATE TABLE education (
    sigun_gu VARCHAR(20),           -- 지역 이름을 나타내는 문자열 (최대 20자)
    extinction_index FLOAT(25) NOT NULL,  -- 소멸 지수 (NULL 값을 허용하지 않음)
    extinction_grade VARCHAR(3) NOT NULL  -- 소멸 등급 (최대 3자, NULL 값을 허용하지 않음)
);



# #primary key (extinction_grade)
show variables like 'secure_file_priv';
load data infile 'C:/MySQL/8.4/Data/Uploads/extinct/merged.csv' into table extinct fields terminated by ',';
