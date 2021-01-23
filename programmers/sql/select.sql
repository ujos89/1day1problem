-- look up all record
SELECT * from ANIMAL_INS

-- look up reversed 
SELECT NAME, DATETIME from ANIMAL_INS order by ANIMAL_ID desc

-- where example
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION='Sick'
SELECT ANIMAL_ID, NAME from ANIMAL_INS where INTAKE_CONDITION!='Aged'

-- use select
SELECT ANIMAL_ID, NAME from ANIMAL_INS

--order by example
SELECT ANIMAL_ID, NAME, DATETIME from ANIMAL_INS order by NAME, DATETIME desc
SELECT NAME from ANIMAL_INS order by DATETIME LIMIT 1