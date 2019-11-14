--количество прилетов и улетов в стране


CREATE OR REPLACE FUNCTION activitycountry(country_ varchar(40), out to_ int, out from_ int) AS $$
BEGIN


to_:=(select count(*)
from passanger_on_flight join fligth on passanger_on_flight.flight_code=fligth.flight_code join airport a1 on fligth.airport_to=a1.iata_code  where a1.country=country_);


from_:=(select count(*)
from passanger_on_flight join fligth on passanger_on_flight.flight_code=fligth.flight_code join airport a1 on fligth.airport_from=a1.iata_code  where a1.country=country_);

END;
$$ LANGUAGE plpgsql;