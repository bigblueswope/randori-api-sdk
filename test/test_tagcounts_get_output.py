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
from randori_api.models.tagcounts_get_output import TagcountsGetOutput  # noqa: E501
from randori_api.rest import ApiException

class TestTagcountsGetOutput(unittest.TestCase):
    """TagcountsGetOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TagcountsGetOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = randori_api.models.tagcounts_get_output.TagcountsGetOutput()  # noqa: E501
        if include_optional :
            return TagcountsGetOutput(
                count = 56, 
                data = [
                    randori_api.models.tagcounts.tagcounts(
                        all_count = 56, 
                        content = '0', 
                        hostname_count = 56, 
                        id = '0', 
                        ip_count = 56, 
                        network_count = 56, 
                        org_id = '0', 
                        poc_count = 56, 
                        service_count = 56, 
                        target_count = 56, )
                    ], 
                offset = 56, 
                total = 56
            )
        else :
            return TagcountsGetOutput(
        )

    def testTagcountsGetOutput(self):
        """Test TagcountsGetOutput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
