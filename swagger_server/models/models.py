# coding: utf-8
from sqlalchemy import ARRAY, BigInteger, Boolean, CheckConstraint, Column, Float, Integer, Numeric, String, Table, Text, text
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql.base import MONEY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CensusBlockGrp(Base):
    __tablename__ = 'census_block_grps'

    gid = Column(Integer, primary_key=True, server_default=text("nextval('census_block_grps_gid_seq'::regclass)"))
    statefp = Column(String(2))
    countyfp = Column(String(3))
    tractce = Column(String(6))
    blkgrpce = Column(String(1))
    geoid = Column(String(12))
    namelsad = Column(String(13))
    mtfcc = Column(String(5))
    funcstat = Column(String(1))
    aland = Column(Numeric)
    awater = Column(Numeric)
    intptlat = Column(String(11))
    intptlon = Column(String(12))
    geom = Column(Geometry(u'MULTIPOLYGON', 4269), index=True)


class CensusBlockGrps2011(Base):
    __tablename__ = 'census_block_grps_2011'

    gid = Column(Integer, primary_key=True, server_default=text("nextval('census_block_grps_2011_gid_seq'::regclass)"))
    statefp = Column(String(2))
    countyfp = Column(String(3))
    tractce = Column(String(6))
    blkgrpce = Column(String(1))
    geoid = Column(String(12))
    namelsad = Column(String(13))
    mtfcc = Column(String(5))
    funcstat = Column(String(1))
    aland = Column(Numeric)
    awater = Column(Numeric)
    intptlat = Column(String(11))
    intptlon = Column(String(12))
    geom = Column(Geometry(u'MULTIPOLYGON', 4269), index=True)


class CensusBlockGrps2016(Base):
    __tablename__ = 'census_block_grps_2016'

    gid = Column(Integer, primary_key=True, server_default=text("nextval('census_block_grps_2016_gid_seq'::regclass)"))
    statefp = Column(String(2))
    countyfp = Column(String(3))
    tractce = Column(String(6))
    blkgrpce = Column(String(1))
    geoid = Column(String(12))
    namelsad = Column(String(13))
    mtfcc = Column(String(5))
    funcstat = Column(String(1))
    aland = Column(Numeric)
    awater = Column(Numeric)
    intptlat = Column(String(11))
    intptlon = Column(String(12))
    geom = Column(Geometry(u'MULTIPOLYGON', 4269), index=True)


t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class OldSocioEconomicDatum(Base):
    __tablename__ = 'old_socio_economic_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('socio_economic_data_id_seq'::regclass)"))
    geoid = Column(Text)
    stusab = Column(Text)
    featurevariablename = Column(Text)
    estresidentialdensity = Column(BigInteger)
    estresidentialdensity25plus = Column(BigInteger)
    estprobabilitynonhispwhite = Column(Float(53))
    estprobabilityhouseholdnonhispwhite = Column(Float(53))
    estprobabilityhighschoolmaxeducation = Column(Float(53))
    estprobabilitynoauto = Column(Float(53))
    estprobabilitynohealthins = Column(Float(53))
    estprobabilityesl = Column(Float(53))
    esthouseholdincome = Column(MONEY)


t_raster_columns = Table(
    'raster_columns', metadata,
    Column('r_table_catalog', String),
    Column('r_table_schema', String),
    Column('r_table_name', String),
    Column('r_raster_column', String),
    Column('srid', Integer),
    Column('scale_x', Float(53)),
    Column('scale_y', Float(53)),
    Column('blocksize_x', Integer),
    Column('blocksize_y', Integer),
    Column('same_alignment', Boolean),
    Column('regular_blocking', Boolean),
    Column('num_bands', Integer),
    Column('pixel_types', ARRAY(Text())),
    Column('nodata_values', ARRAY(Float(precision=53))),
    Column('out_db', Boolean),
    Column('extent', Geometry),
    Column('spatial_index', Boolean)
)


t_raster_overviews = Table(
    'raster_overviews', metadata,
    Column('o_table_catalog', String),
    Column('o_table_schema', String),
    Column('o_table_name', String),
    Column('o_raster_column', String),
    Column('r_table_catalog', String),
    Column('r_table_schema', String),
    Column('r_table_name', String),
    Column('r_raster_column', String),
    Column('overview_factor', Integer)
)


class SocioEconomicDatum(Base):
    __tablename__ = 'socio_economic_data'

    id = Column(Integer, primary_key=True, server_default=text("nextval('socio_economic_data_id_seq1'::regclass)"))
    estresidentialdensity = Column(BigInteger)
    geoid = Column(Text, unique=True)
    estresidentialdensity25plus = Column(BigInteger)
    estresidentialdensity_se = Column(Float(53))
    estresidentialdensity25plus_se = Column(Float(53))
    estprobabilitynonhispwhite = Column(Float(53))
    estprobabilitynonhispwhite_se = Column(Float(53))
    estprobabilityhighschoolmaxeducation = Column(Float(53))
    estprobabilityhighschoolmaxeducation_se = Column(Float(53))
    estprobabilityesl = Column(Float(53))
    estprobabilityesl_se = Column(Float(53))
    esthouseholdincome = Column(MONEY)
    esthouseholdincome_se = Column(Float(53))
    estprobabilitynoauto = Column(Float(53))
    estprobabilitynoauto_se = Column(Float(53))
    estprobabilitynohealthins = Column(Float(53))
    estprobabilitynohealthins_se = Column(Float(53))


class SocioEconomicData2019(Base):
    __tablename__ = 'socio_economic_data_2019'

    id = Column(Integer, primary_key=True, server_default=text("nextval('socio_economic_data_2019_id_seq'::regclass)"))
    bgid2016 = Column(Text, unique=True)
    bgid2011 = Column(Text, unique=True)
    bgid2010 = Column(Text)
    latitude = Column(Float(53))
    longitude = Column(Float(53))
    tract = Column(Text)
    st_cnty = Column(Text)
    stusab = Column(Text)
    state_code = Column(Text)
    county_name = Column(Text)
    cbsa_code = Column(Text)
    cbsa_title = Column(Text)
    csa_code = Column(Text)
    csa_title = Column(Text)
    metro_micro = Column(Text)
    urban_code = Column(Text)
    urban_name = Column(Text)
    area_type = Column(Text)
    place_code = Column(Text)
    place_name = Column(Text)
    area_kmsq = Column(Float(53))
    congressional_district = Column(Text)
    state_upper_legislative_district = Column(Text)
    state_lower_legislative_district = Column(Text)
    unified_school_district = Column(Text)
    hospital_service_area_code = Column(Text)
    hospital_service_area_city = Column(Text)
    hospital_service_area_state = Column(Text)
    hospital_referral_area_code = Column(Text)
    hospital_referral_area_city = Column(Text)
    hospital_referral_area_state = Column(Text)
    estpopulation_2011 = Column(BigInteger)
    estpopulation_2016 = Column(BigInteger)
    estpopulation_2016se = Column(Float(53))
    estresidentialdensity_2011 = Column(Float(53))
    estresidentialdensity_2016 = Column(Float(53))
    estresidentialdensity_2016se = Column(Float(53))
    estmedianhouseholdincome_2011 = Column(MONEY)
    estmedianhouseholdincome_2016 = Column(MONEY)
    estmedianhouseholdincome_2016se = Column(Float(53))
    estpropnonhispwhite_2011 = Column(Float(53))
    estpropnonhispwhite_2016 = Column(Float(53))
    estpropnonhispwhite_2016se = Column(Float(53))
    estprophighschoolmaxeducation_2011 = Column(Float(53))
    estprophighschoolmaxeducation_2016 = Column(Float(53))
    estprophighschoolmaxeducation_2016se = Column(Float(53))
    estpropnoauto_2011 = Column(Float(53))
    estpropnoauto_2016 = Column(Float(53))
    estpropnoauto_2016se = Column(Float(53))
    estpropesl_2011 = Column(Float(53))
    estpropesl_2016 = Column(Float(53))
    estpropesl_2016se = Column(Float(53))
    estpropnohealthins_2016 = Column(Float(53))
    estpropnohealthins_2016se = Column(Float(53))
    estpropfemalehouseholdnospouse_2011 = Column(Float(53))
    estpropfemalehouseholdnospouse_2016 = Column(Float(53))
    estpropfemalehouseholdnospouse_2016se = Column(Float(53))
    estpropfemalehouseholdfamilychild_2011 = Column(Float(53))
    estpropfemalehouseholdfamilychild_2016 = Column(Float(53))
    estpropfemalehouseholdfamilychild_2016se = Column(Float(53))
    estpropfemalehouseholdanychild_2011 = Column(Float(53))
    estpropfemalehouseholdanychild_2016 = Column(Float(53))
    estpropfemalehouseholdanychild_2016se = Column(Float(53))
    estprophighschooldropout_2011 = Column(Float(53))
    estprophighschooldropout_2016 = Column(Float(53))
    estprophighschooldropoutnowork_2011 = Column(Float(53))
    estprophighschooldropoutnowork_2016 = Column(Float(53))
    estprophouseholdssi_2011 = Column(Float(53))
    estprophouseholdssi_2016 = Column(Float(53))
    estprophouseholdssi_2016se = Column(Float(53))
    estprophouseholdpa_2011 = Column(Float(53))
    estprophouseholdpa_2016 = Column(Float(53))
    estprophouseholdpa_2016se = Column(Float(53))
    estpropmalelittlework_2011 = Column(Float(53))
    estpropmalelittlework_2016 = Column(Float(53))


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))
