import sys
from configparser import ConfigParser
from datetime import datetime, timedelta
from sqlalchemy import extract, func, cast
from geoalchemy2 import Geography

import pytz
from swagger_server.controllers import Session
from flask import jsonify
from swagger_server.models.models import SocioEconomicDatum, CensusBlockGrp

parser = ConfigParser()
parser.read('swagger_server/ini/connexion.ini')
sys.path.append(parser.get('sys-path', 'exposures'))
sys.path.append(parser.get('sys-path', 'controllers'))
from enum import Enum


class MeasurementType(Enum):
    # lat: 0 to +/- 90, lon: 0 to +/- 180 as lat,lon

    LATITUDE = '^[+-]?(([1-8]?[0-9])(\.[0-9]+)?|90(\.0+)?)$'
    LONGITUDE = '^[+-]?((([1-9]?[0-9]|1[0-7][0-9])(\.[0-9]+)?)|180(\.0+)?)$'

    def isValid(self, measurement):
        import re
        if re.match(self.value, str(measurement)) is None:
            return False
        else:
            return True

class SocioEconExposures(object):

    def is_valid_lat_lon(self, **kwargs):
        # lat: 0 to +/- 90, lon: 0 to +/- 180 as lat,lon
        if not MeasurementType.LATITUDE.isValid(kwargs.get('latitude')):
            return False, ('Invalid parameter', 400, {'x-error': 'Invalid parameter: latitude'})
        if not MeasurementType.LONGITUDE.isValid(kwargs.get('longitude')):
            return False, ('Invalid parameter', 400, {'x-error': 'Invalid parameter: longitude'})

        return True, ''

    def validate_parameters(self, **kwargs):
        lat_lon_valid, msg = self.is_valid_lat_lon(**kwargs)

        if not lat_lon_valid:
            return False, msg
        else:
            return True, ''

    def get_values(self, **kwargs):
        # latitude, longitude

        # validate input from user
        is_valid, message = self.validate_parameters(**kwargs)
        if not is_valid:
            return message

        # create data object
        data = {}
        # data['values'] = []

        # retrieve query result for each lat,lon pair and add to data object
        lat = kwargs.get('latitude')
        lon = kwargs.get('longitude')

        session = Session()

        # given this lat lon, find the census tract that contains it.
        query = session.query(CensusBlockGrp.geoid). \
                            filter(func.ST_Contains(CensusBlockGrp.geom,
                                    func.ST_GeomFromText("POINT(" + str(lon) + " " + str(lat) + ")", 4269)))
        result = session.execute(query)
        for query_return_values in result:
            geoid = query_return_values[0]

        # daily resolution of data - return only matched hours for date range
        query = session.query(SocioEconomicDatum.id,
                              SocioEconomicDatum.geoid,
                              SocioEconomicDatum.estresidentialdensity,
                              SocioEconomicDatum.estresidentialdensity_se,
                              SocioEconomicDatum.estresidentialdensity25plus,
                              SocioEconomicDatum.estresidentialdensity25plus_se,
                              SocioEconomicDatum.estprobabilitynonhispwhite,
                              SocioEconomicDatum.estprobabilitynonhispwhite_se,
                              SocioEconomicDatum.estprobabilityhighschoolmaxeducation,
                              SocioEconomicDatum.estprobabilityhighschoolmaxeducation_se,
                              SocioEconomicDatum.estprobabilitynoauto,
                              SocioEconomicDatum.estprobabilitynoauto_se,
                              SocioEconomicDatum.estprobabilitynohealthins,
                              SocioEconomicDatum.estprobabilitynohealthins_se,
                              SocioEconomicDatum.estprobabilityesl,
                              SocioEconomicDatum.estprobabilityesl_se,
                              SocioEconomicDatum.esthouseholdincome,
                              SocioEconomicDatum.esthouseholdincome_se). \
                                  filter(SocioEconomicDatum.geoid.like("%" + geoid))

        session.close()
	
        for query_return_values in query:
            # data['values'].append({'latitude': lat,
            data.update({'latitude': lat,
                                   'longitude': lon,
                                   'geoid': query_return_values[1],
                                   'EstTotalPop': int(query_return_values[2]),
                                   'EstTotalPop_SE': float(query_return_values[3]),
                                   'EstTotalPop25Plus': int(query_return_values[4]),
                                   'EstTotalPop25Plus_SE': float(query_return_values[5]),
                                   'EstPropPersonsNonHispWhite': float(query_return_values[6]),
                                   'EstPropPersonsNonHispWhite_SE': float(query_return_values[7]),
                                   'EstPropPersons25PlusHighSchoolMax': float(query_return_values[8]),
                                   'EstPropPersons25PlusHighSchoolMax_SE': float(query_return_values[9]),
                                   'EstPropHouseholdsNoAuto': float(query_return_values[10]),
                                   'EstPropHouseholdsNoAuto_SE': float(query_return_values[11]),
                                   'EstPropPersonsNoHealthIns': float(query_return_values[12]),
                                   'EstPropPersonsNoHealthIns_SE': float(query_return_values[13]),
                                   'EstPropPersons5PlusNoEnglish': float(query_return_values[14]),
                                   'EstPropPersons5PlusNoEnglish_SE': float(query_return_values[15]),
                                   'MedianHouseholdIncome': query_return_values[16],
                                   'MedianHouseholdIncome_SE': query_return_values[17]})
            break

        return jsonify(data)
