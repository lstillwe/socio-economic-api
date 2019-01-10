-- Format
-- EstResidentialDensity,GEOID,EstResidentialDensity25Plus,EstResidentialDensity_SE,EstResidentialDensity25Plus_SE,EstProbabilityNonHispWhite,EstProbabilityNonHispWhite_SE,EstProbabilityHighSchoolMaxEducation,EstProbabilityHighSchoolMaxEducation_SE,EstProbabilityESL,EstProbabilityESL_SE,EstHouseholdIncome,EstHouseholdIncome_SE,EstProbabilityNoAuto,EstProbabilityNoAuto_SE,EstProbabilityNoHealthIns,EstProbabilityNoHealthIns_SE
-- 745,15000US010010201001,474,137.5303603,76.00624974,0.763758389,0.105181283,0.53164557,0.076480429,0.075070822,0.040387049,29744,20687.82917,0.038732394,0.039252128,0.183892617,0.063328335`

-- create a temporary table for holding the raw data
CREATE TEMP TABLE tmp (
    EstResidentialDensity TEXT,
    GEOID TEXT,
    EstResidentialDensity25Plus TEXT,
    EstResidentialDensity_SE TEXT,
    EstResidentialDensity25Plus_SE TEXT,
    EstProbabilityNonHispWhite TEXT,
    EstProbabilityNonHispWhite_SE TEXT,
    EstProbabilityHighSchoolMaxEducation TEXT,
    EstProbabilityHighSchoolMaxEducation_SE TEXT,
    EstProbabilityESL TEXT,
    EstProbabilityESL_SE TEXT,
    EstHouseholdIncome TEXT,
    EstHouseholdIncome_SE TEXT,
    EstProbabilityNoAuto TEXT,
    EstProbabilityNoAuto_SE TEXT,
    EstProbabilityNoHealthIns TEXT,
    EstProbabilityNoHealthIns_SE TEXT
);

-- copy the raw data from sample csv file
COPY tmp FROM '/projects/datatrans/ACS_Data/Appold_renci_US_replse_20October18.csv' DELIMITER ',' CSV HEADER ;

-- create a table to load data into named socio_economic_data
CREATE TABLE IF NOT EXISTS socio_economic_data (
    id SERIAL UNIQUE PRIMARY KEY,
    EstResidentialDensity BIGINT,
    geoid TEXT,
    EstResidentialDensity25Plus BIGINT,
    EstResidentialDensity_SE FLOAT,
    EstResidentialDensity25Plus_SE FLOAT,
    EstProbabilityNonHispWhite FLOAT,
    EstProbabilityNonHispWhite_SE FLOAT,
    EstProbabilityHighSchoolMaxEducation FLOAT,
    EstProbabilityHighSchoolMaxEducation_SE FLOAT,
    EstProbabilityESL FLOAT,
    EstProbabilityESL_SE FLOAT,
    EstHouseholdIncome MONEY,
    EstHouseholdIncome_SE FLOAT,
    EstProbabilityNoAuto FLOAT,
    EstProbabilityNoAuto_SE FLOAT,
    EstProbabilityNoHealthIns FLOAT,
    EstProbabilityNoHealthIns_SE FLOAT
);

-- load the socio_economic_data table with properly formatted data
INSERT INTO socio_economic_data (EstResidentialDensity, geoid, EstResidentialDensity25Plus, EstResidentialDensity_SE, EstResidentialDensity25Plus_SE, EstProbabilityNonHispWhite, EstProbabilityNonHispWhite_SE, EstProbabilityHighSchoolMaxEducation, EstProbabilityHighSchoolMaxEducation_SE, EstProbabilityESL,  EstProbabilityESL_SE, EstHouseholdIncome, EstHouseholdIncome_SE, EstProbabilityNoAuto, EstProbabilityNoAuto_SE, EstProbabilityNoHealthIns, EstProbabilityNoHealthIns_SE)
    SELECT
      cast(EstResidentialDensity as BIGINT),
      GEOID,
      cast(EstResidentialDensity25Plus as BIGINT),
      cast(EstResidentialDensity_SE as FLOAT),
      cast(EstResidentialDensity25Plus_SE as FLOAT),
      cast(EstProbabilityNonHispWhite as FLOAT),
      cast(EstProbabilityNonHispWhite_SE as FLOAT),
      cast(EstProbabilityHighSchoolMaxEducation as FLOAT),
      cast(EstProbabilityHighSchoolMaxEducation_SE as FLOAT),
      cast(EstProbabilityESL as FLOAT),
      cast(EstProbabilityESL_SE as FLOAT),
      cast(EstHouseholdIncome as MONEY),
      cast(EstHouseholdIncome_SE as FLOAT),
      cast(EstProbabilityNoAuto as FLOAT),
      cast(EstProbabilityNoAuto_SE as FLOAT),
      cast(EstProbabilityNoHealthIns as FLOAT),
      cast(EstProbabilityNoHealthIns_SE as FLOAT)
    FROM tmp;

-- drop the temporary table
DROP TABLE tmp;

-- set owner to datatrans user
ALTER TABLE socio_economic_data OWNER TO datatrans;

-- display a sample of contents to user
SELECT * FROM socio_economic_data ORDER BY id ASC LIMIT 10;
