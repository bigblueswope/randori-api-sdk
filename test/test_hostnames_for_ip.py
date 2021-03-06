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
import datetime

import randori_api
from randori_api.models.hostnames_for_ip import HostnamesForIp  # noqa: E501
from randori_api.rest import ApiException

class TestHostnamesForIp(unittest.TestCase):
    """HostnamesForIp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HostnamesForIp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.hostnames_for_ip.HostnamesForIp()  # noqa: E501
        if include_optional :
            return HostnamesForIp(
                affiliation_state = 'None', 
                confidence = 56, 
                deleted = True, 
                hostname = '0', 
                hostname_id = '0', 
                id = '0', 
                impact_score = 'None', 
                ip_id = '0', 
                last_seen = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                lens_id = '0', 
                lens_view = '0', 
                org_id = '0', 
                perspective = '0', 
                perspective_name = '0', 
                status = 'None'
            )
        else :
            return HostnamesForIp(
                id = '0',
                org_id = '0',
        )

    def testHostnamesForIp(self):
        """Test HostnamesForIp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
