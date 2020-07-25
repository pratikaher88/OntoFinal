-- CREATE USER paher;
CREATE ROLE paher ;


CREATE DATABASE hospital1;
GRANT ALL PRIVILEGES ON DATABASE hospital1 TO paher;

-- CREATE TABLE NeuroData (
-- 	ID serial PRIMARY KEY,
-- 	patient_id VARCHAR (255) NOT NULL,
-- 	doctor_id VARCHAR (255),
-- 	date DATE ,
--     doctors_note VARCHAR (255),
--     lab_results VARCHAR (255),
--     scan_results VARCHAR (255),
--     neuro_sugery_details VARCHAR (255)
-- );


INSERT INTO NeuroData (patient_id, doctor_id, date,doctors_note, lab_results, scan_results, neuro_sugery_details )
VALUES ('111','222','01-01-2020', 'this is it','dsfs dsfg','sdfsfd sdf','fsd ddfg');

INSERT INTO NeuroData (patient_id, doctor_id, date,doctors_note, lab_results, scan_results, neuro_sugery_details )
VALUES ('432','222','01-01-2020', 'this is it','dsfs dsfg','sdfsfd sdf','fsd ddfg');


