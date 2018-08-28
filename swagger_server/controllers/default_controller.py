import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_values(latitude, longitude):  # noqa: E501
    """provides ACS values

    By passing in a location specification (lat, lon), you can retrieve the the ACS Values for that location  # noqa: E501

    :param latitude: latitude in decimal degrees format, ie: 35.7
    :type latitude: str
    :param longitude: longitude in decimal degrees format, ie: -80.33
    :type longitude: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
