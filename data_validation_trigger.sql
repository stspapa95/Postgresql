-- data validation before inserted or updated on tablename
CREATE FUNCTION tablename() RETURNS trigger AS $$
BEGIN
IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
	IF NEW.result <> 'value 1' AND NEW.result <> 'value 2' AND NEW.result <> 'value 3' THEN
		RAISE EXCEPTION 'Requirements not met';
	ELSE
		NEW.result := NEW.result;
	END IF;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER val_rs BEFORE INSERT OR UPDATE ON raptor_surveys FOR EACH ROW EXECUTE PROCEDURE validate_raptor_surveys();
