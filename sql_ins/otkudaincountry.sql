--из каких стран(список и сколько их) едут в конкретную страну


CREATE OR REPLACE FUNCTION otkudaincountry(country_ VARCHAR(40) ) RETURNS table(country VARCHAR(40),  count bigint) AS $$
BEGIN
return query
select a1.country, count(*)
from passanger_on_flight join fligth on passanger_on_flight.flight_code=fligth.flight_code join airport a1 on fligth.airport_from=a1.iata_code  join airport a2 on fligth.airport_to=a2.iata_code   where a2.country=country_ group by a1.country  order by count DESC limit 10;

END;
$$ LANGUAGE plpgsql;