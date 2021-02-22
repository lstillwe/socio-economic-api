import sys

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
#from swagger_server.models.models import SocioEconomicDatum  # noqa: E501
from swagger_server.models.models import SocioEconomicData2019  # noqa: E501
from swagger_server import util
from configparser import ConfigParser
from sqlalchemy import exists, or_, func

from swagger_server.controllers import Session
from flask import jsonify

parser = ConfigParser()
parser.read('swagger_server/ini/connexion.ini')
sys.path.append(parser.get('sys-path', 'exposures'))
sys.path.append(parser.get('sys-path', 'controllers'))


def get_values(latitude, longitude, years):  # noqa: E501
    """2016 ACS (American Community Survey) Socio-Economic data

    By passing in a location specification (lat, lon) and a year range, you can retrieve the the ACS Values for that location and year range

    :param latitude: latitude in decimal degrees format, ie: 35.7
    :type latitude: str
    :param longitude: longitude in decimal degrees format, ie: -80.33
    :type longitude: str
    :param years: range of years for socio-econ data 
    :type years: str
    : enum:
        - All (2007-2016)
        - 2007-2011
        - 2012-2016

    :rtype: InlineResponse200
    """
    from swagger_server.socio_exposures.socio_econ import SocioEconExposures
    socio = SocioEconExposures()
    kwargs = locals()
    data = socio.get_values(**kwargs)

    return data
