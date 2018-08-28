-- Format
-- GEOID,STUSAB,FeatureVariableName,EstResidentialDensity,EstResidentialDensity25Plus,EstProbabilityNonHispWhite,EstProbabilityHouseholdNonHispWhite,EstProbabilityHighSchoolMaxEducation,EstProbabilityNoAuto,EstProbabilityNoHealthIns,EstProbabilityESL,EstHouseholdIncome
-- 15000US020130001001,ak,,906,773,0.173289183,0.324786325,0.593790427,0.504273504,0.682574917,0.646599777,49750

-- create a temporary table for holding the raw data
CREATE TEMP TABLE tmp (
    GEOID TEXT,
    STUSAB TEXT,
    FeatureVariableName TEXT,
    EstResidentialDensity TEXT BIGINT,
    EstResidentialDensity25Plus TEXT BIGINT,
    EstProbabilityNonHispWhite TEXT FLOAT,
    EstProbabilityHouseholdNonHispWhite TEXT FLOAT,
    EstProbabilityHighSchoolMaxEducation TEXT FLOAT,
    EstProbabilityNoAuto TEXT FLOAT,
    EstProbabilityNoHealthIns TEXT FLOAT,
    EstProbabilityESL TEXT FLOAT,
    EstHouseholdIncome TEXT MONEY
);

-- copy the raw data from sample csv file
COPY tmp FROM '/projects/datatrans/ACS_Data/ACS_USA_2016.csv' DELIMITER ',' CSV HEADER ;

-- create a table to load data into named socio_economic_data
CREATE TABLE IF NOT EXISTS socio_economic_data (
    id SERIAL UNIQUE PRIMARY KEY,
    geoid TEXT,
    stusab TEXT,
    FeatureVariableName TEXT,
    EstResidentialDensity BIGINT,
    EstResidentialDensity25Plus BIGINT,
    EstProbabilityNonHispWhite FLOAT,
    EstProbabilityHouseholdNonHispWhite FLOAT,
    EstProbabilityHighSchoolMaxEducation FLOAT,
    EstProbabilityNoAuto FLOAT,
    EstProbabilityNoHealthIns FLOAT,
    EstProbabilityESL FLOAT,
    EstHouseholdIncome MONEY
);

-- load the socio_economic_data table with properly formatted data
INSERT INTO socio_economic_data (geoid, stusab, FeatureVariableName, EstResidentialDensity, EstResidentialDensity25Plus, EstProbabilityNonHispWhite, EstProbabilityHouseholdNonHispWhite, EstProbabilityHighSchoolMaxEducation, EstProbabilityNoAuto, EstProbabilityNoHealthIns, EstProbabilityESL, EstHouseholdIncome)
    SELECT
      GEOID,
      STUSAB,
      FeatureVariableName,
      cast(EstResidentialDensity as BIGINT),
      cast(EstResidentialDensity25Plus as BIGINT),
      cast(EstProbabilityNonHispWhite as FLOAT),
      cast(EstProbabilityHouseholdNonHispWhite as FLOAT),
      cast(EstProbabilityHighSchoolMaxEducation as FLOAT),
      cast(EstProbabilityNoAuto as FLOAT),
      cast(EstProbabilityNoHealthIns as FLOAT),
      cast(EstProbabilityESL as FLOAT),
      cast(EstHouseholdIncome as MONEY)
    FROM tmp;

-- drop the temporary table
DROP TABLE tmp;

-- set owner to datatrans user
ALTER TABLE socio_economic_data OWNER TO datatrans;

-- display a sample of contents to user
SELECT * FROM socio_economic_data ORDER BY date ASC LIMIT 10;
