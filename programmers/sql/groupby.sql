--group by name
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) as count
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE

--having example
SELECT NAME, COUNT(NAME) as count
from ANIMAL_INS
group by NAME
having count > 1
order by NAME

--having example2
SELECT HOUR(DATETIME) as HOUR, COUNT(*) as COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR >=9 and HOUR <= 19
order by HOUR

--set example
SET @HOUR := -1;
SELECT  (@HOUR := @HOUR + 1) as HOUR,
        (SELECT COUNT(*)
         from ANIMAL_OUTS
         where HOUR(DATETIME) = @HOUR
        )as COUNT
from ANIMAL_OUTS
where @HOUR < 23;