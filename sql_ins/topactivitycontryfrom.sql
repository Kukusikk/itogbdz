--топ стран по количеству улетов из них

CREATE OR REPLACE FUNCTION topactivitycontryfrom() RETURNS table(country VARCHAR(40), count bigint) AS $$
BEGIN

return query
select airport.country, count(*)
from passanger_on_flight join fligth on passanger_on_flight.flight_code=fligth.flight_code join airport on fligth.airport_from=airport.iata_code group by airport.country order by count DESC limit 10;

END;
$$ LANGUAGE plpgsql;