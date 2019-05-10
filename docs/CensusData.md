## Census Data details for Socio-Economic API

The data originated with three source files:
  1.	trans_geo_cross,
  2.	Appold_renci_US_22August, and
  3.	Appold_renci_US_replse_20October18.
      
The first file contains a set of geographic identifiers, while the second two files contain the socio-demographic variables. The third file differs from the second file in that it includes standard errors for each of the socio-demographic estimates. The variable values on that file were calculated from the 2012–-2016 (five-year summary file) of the American Community Survey. Because each of the values in the ACS data files represent summary statistics calculated from sample survey data for each Block Group, different samples yield somewhat different values. Therefore, the US Census Bureau generates 80 replicate values for selected variables. These provide the basis for the estimated standard errors of the estimates.

The second and third files contain slightly different values in some cases, but there is no reason to link them with each other. Because there are no standard errors, the second file is easier to use and adequate for most purposes. However, it may be useful for some researchers to link one of the data files with the file containing the geographic identifiers. GEOID provides a common identifier. Removing the first seven characters from GEOID allows for an easy linkage to ESRI (ArcInfo), Quantum, and other GIS software.

Locations are expressed using WGS84 decimal format. WGS84 is the World Geodetic System for expressing latitude and longitude. For example, the Statue of Liberty in New York City is at latitude 40.689249 and longitude -74.044500.

Additional details on the variables are provided in the tables below.

|This file contains geographic identifiers only||||
|---|---|---|---|
|geoid|Full Census block group ID|This is the key which links this geographic identifier file to the data files
|state|FIPS State code
|stusab|State abbreviation
|county|FIPS County code
|cntyname|County name
|tract|Tract
|bg|Block group
|cbsa13|FIPS CBSA (2013) code|Census Core-based Statistical Area code
|cbsatype13|CBSA type (2013)|Metropolitan area/Micropolitan area/Rural (last is blank)
|cbsaname|2013 CBSA name
|ur|Urban/rural|Urban or rural
|ua|FIPS Urban area code
|uaname|UA/Urban cluster name
|placefp14|FIPS Place (2014) code
|placenm14|Place name 2014
|cd116|116th Congressional district|These need to be used in tandem with state identifiers|These are identified by code only
|sldu16|State legislative district, upper (2016)|Format may vary by state|These are identified by code only
|sldl16|State legislative district, lower (2016)|Format may vary by state|These are identified by code only
|hsa|Hospital service areas (2016) code
|hsaname|Hospital service areas 2016 name


|These two files contain slightly different versions of the socio-economic data||||
|---|---|---|---|
|Appold_renci_US_22August|Appold_renci_US_replse_20October18
|**Basic data**||||
|GEOID|GEOID|Full Census block group ID|to aid linking with other data and mapping
|STUSAB||Two-letter state identifier
|total_pop2016|tot_pop|total population in block group
|total_25plus|pop25plus|population aged 25 and up in block group
|nHwtindiv|prp_nHwh|proportion of the block group population that is non-Hispanic white|undefined for block groups with 0 population
|median_HH_inc|median_inc|median household income|undefined for block groups with 0 households; subject to Census disclosure rules
|prp_nHwHHs||proportion of the block group households that are non-Hispanic white
|prp_HSminus|prp_HSmin|proportion of the block group population aged 25 and up with a HS diploma or less|undefined for block groups with 0 population 25 and older
|prp_no_auto|prp_noveh|proportion of the block group households with no automobile|undefined for block groups with 0 households
|prp_not_insured|prp_noins|proportion of the block group population with no health insurance|undefined for block groups with 0 population; no information for approximately 20 blockgroups with 0 households
|prp_foreign|prp_forlang|proportion of the block group population aged 5 plus sometimes speaking a language other than English at home|undefined for block groups with 0 population
||**Standard errors**
|tot_pop_se|these correspond to the estimates above|there are s.e.s for zero estimates but these are coded missing if the estimates are missing due to data suppression
||pop25plus_se
||prp_nHwh_se
||median_inc_se
||prp_HSmin_se
||prp_noveh_se
||prp_noins_se
||prp_forlang_se
|||||
|||||
