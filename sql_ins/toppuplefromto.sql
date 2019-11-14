--самые активные пассажиры между странами
CREATE OR REPLACE FUNCTION toppuplefromto(from_ varchar(40), to_ varchar(40)) RETURNS table(first_name VARCHAR(40), last_name VARCHAR(40), id int , count bigint) AS $$
BEGIN

return query select a.first_name, a.last_name,a.id ,count(a.date) from (select *
from passanger_on_flight join passanger on passanger_on_flight.pasanger_code = CAST(passanger.id as VARCHAR(20))
join fligth on passanger_on_flight.flight_code = fligth.flight_code
where airport_from in (select iata_code from airport where country = from_) and
airport_to in (select iata_code from airport where country = to_)
union all
(select *
from passanger_on_flight join passanger on passanger_on_flight.pasanger_code = CAST(passanger.id as VARCHAR(20))
join fligth on passanger_on_flight.flight_code = fligth.flight_code
where airport_to in (select iata_code from airport where country = to_) and
airport_from in (select iata_code from airport where country = from_))) as a group by a.first_name, a.last_name , a.id order by count DESC ;

END;
$$ LANGUAGE plpgsql;