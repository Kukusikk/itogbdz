
 --самые активные пассажиры

  CREATE OR REPLACE FUNCTION toactivitypassanger() RETURNS table(first_name VARCHAR(40), last_name VARCHAR(40), count bigint) AS $$
BEGIN

return query select a.first_name, a.last_name, count(a.date) from (select *
from passanger_on_flight join passanger on passanger_on_flight.pasanger_code = CAST(passanger.id as VARCHAR(20))
join fligth on passanger_on_flight.flight_code = fligth.flight_code) as a group by a.first_name, a.last_name order by count DESC limit 20;

END;
$$ LANGUAGE plpgsql;