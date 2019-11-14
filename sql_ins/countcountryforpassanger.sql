--на вход подаем номер паспорта пассажира а на выходе имеем список стран в которых он был и сколько раз
CREATE OR REPLACE FUNCTION countcountryforpassanger(number_doc VARCHAR(20) ) RETURNS table(country VARCHAR(40),  count bigint) AS $$
BEGIN
return query
select airport.country , count (*)
from from_csv join airport on from_csv.destination=airport.city  where from_csv.passengerdocument=number_doc group by airport.country;


END;
$$ LANGUAGE plpgsql;










