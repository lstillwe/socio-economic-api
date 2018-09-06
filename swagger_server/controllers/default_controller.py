import sys

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.models import SocioEconomicDatum  # noqa: E501
from swagger_server import util
from configparser import ConfigParser
from sqlalchemy import exists, or_, func

from swagger_server.controllers import Session
from flask import jsonify

parser = ConfigParser()
parser.read('swagger_server/ini/connexion.ini')
sys.path.append(parser.get('sys-path', 'exposures'))
sys.path.append(parser.get('sys-path', 'controllers'))


def get_values(latitude, longitude):  # noqa: E501
    """2016 ACS (American Community Survey) Socio-Economic data

    By passing in a location specification (lat, lon), you can retrieve the the ACS Values for that location  # noqa: E501

    :param latitude: latitude in decimal degrees format, ie: 35.7
    :type latitude: str
    :param longitude: longitude in decimal degrees format, ie: -80.33
    :type longitude: str

    :rtype: InlineResponse200
    """
    from swagger_server.socio_exposures.socio_econ import SocioEconExposures
    socio = SocioEconExposures()
    kwargs = locals()
    data = socio.get_values(**kwargs)

    return data
