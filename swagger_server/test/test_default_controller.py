# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_values(self):
        """Test case for get_values

        provides ACS values
        """
        query_string = [('latitude', 'latitude_example'),
                        ('longitude', 'longitude_example')]
        response = self.client.open(
            '/proximity_api/socio-environmental-exposures-api/1.0.0/values',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
