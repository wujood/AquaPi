# coding: utf-8

"""
    AquaPi Swagger API

    REST API for the AquaPi

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.put_api import PutApi


class TestPutApi(unittest.TestCase):
    """ PutApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.put_api.PutApi()

    def tearDown(self):
        pass

    def test_put_component_settings(self):
        """
        Test case for put_component_settings

        Sets a new component settings
        """
        pass

    def test_put_fishes(self):
        """
        Test case for put_fishes

        Sets the fishes that are in the aquarium
        """
        pass

    def test_put_plants(self):
        """
        Test case for put_plants

        Sets the number of plants
        """
        pass

    def test_put_push_configuration(self):
        """
        Test case for put_push_configuration

        Sets new PushConfigurations
        """
        pass


if __name__ == '__main__':
    unittest.main()