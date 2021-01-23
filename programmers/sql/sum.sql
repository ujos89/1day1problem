-- get maximum value
SELECT DATETIME from ANIMAL_INS order by DATETIME desc LIMIT 1

--get minimum value
SELECT DATETIME from ANIMAL_INS order by DATETIME LIMIT 1

--count method
SELECT COUNT(*) from ANIMAL_INS

--except duplicate
SELECT COUNT(DISTINCT NAME) from ANIMAL_INS