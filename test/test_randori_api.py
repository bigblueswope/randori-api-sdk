# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import randori_api
from randori_api.api.randori_api import RandoriApi  # noqa: E501
from randori_api.rest import ApiException


class TestRandoriApi(unittest.TestCase):
    """RandoriApi unit test stubs"""

    def setUp(self):
        self.api = randori_api.api.randori_api.RandoriApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_detection_target(self):
        """Test case for get_detection_target

        """
        pass

    def test_get_detections_for_target(self):
        """Test case for get_detections_for_target

        """
        pass

    def test_get_hostname(self):
        """Test case for get_hostname

        """
        pass

    def test_get_hostnames_for_ip(self):
        """Test case for get_hostnames_for_ip

        """
        pass

    def test_get_ip(self):
        """Test case for get_ip

        """
        pass

    def test_get_ips_for_hostname(self):
        """Test case for get_ips_for_hostname

        """
        pass

    def test_get_ips_for_network(self):
        """Test case for get_ips_for_network

        """
        pass

    def test_get_ips_for_service(self):
        """Test case for get_ips_for_service

        """
        pass

    def test_get_network(self):
        """Test case for get_network

        """
        pass

    def test_get_ports_for_ip(self):
        """Test case for get_ports_for_ip

        """
        pass

    def test_get_service(self):
        """Test case for get_service

        """
        pass

    def test_get_single_hostname(self):
        """Test case for get_single_hostname

        """
        pass

    def test_get_single_hostnames_for_ip(self):
        """Test case for get_single_hostnames_for_ip

        """
        pass

    def test_get_single_ip(self):
        """Test case for get_single_ip

        """
        pass

    def test_get_single_ips_for_hostname(self):
        """Test case for get_single_ips_for_hostname

        """
        pass

    def test_get_single_ips_for_network(self):
        """Test case for get_single_ips_for_network

        """
        pass

    def test_get_single_ips_for_service(self):
        """Test case for get_single_ips_for_service

        """
        pass

    def test_get_single_network(self):
        """Test case for get_single_network

        """
        pass

    def test_get_single_ports_for_ip(self):
        """Test case for get_single_ports_for_ip

        """
        pass

    def test_get_single_service(self):
        """Test case for get_single_service

        """
        pass

    def test_get_single_target(self):
        """Test case for get_single_target

        """
        pass

    def test_get_statistics(self):
        """Test case for get_statistics

        """
        pass

    def test_get_target(self):
        """Test case for get_target

        """
        pass


if __name__ == '__main__':
    unittest.main()
