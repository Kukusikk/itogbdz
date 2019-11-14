
--топ стран по количеству прилетов в них

CREATE OR REPLACE FUNCTION topactivitycontryto() RETURNS table(country VARCHAR(40), count bigint) AS $$
BEGIN

return query
select airport.country, count(*)
from passanger_on_flight join fligth on passanger_on_flight.flight_code=fligth.flight_code join airport on fligth.airport_to=airport.iata_code group by airport.country order by count DESC limit 20;

END;
$$ LANGUAGE plpgsql;