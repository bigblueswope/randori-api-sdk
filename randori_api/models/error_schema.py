# coding: utf-8

"""
    Randori API

    Endpoints accessible using API tokens  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@randori.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ErrorSchema(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'reason': 'str',
        'ref': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'ref': 'ref'
    }

    def __init__(self, reason=None, ref=None):  # noqa: E501
        """ErrorSchema - a model defined in OpenAPI"""  # noqa: E501

        self._reason = None
        self._ref = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if ref is not None:
            self.ref = ref

    @property
    def reason(self):
        """Gets the reason of this ErrorSchema.  # noqa: E501

        explaination of the error  # noqa: E501

        :return: The reason of this ErrorSchema.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ErrorSchema.

        explaination of the error  # noqa: E501

        :param reason: The reason of this ErrorSchema.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def ref(self):
        """Gets the ref of this ErrorSchema.  # noqa: E501

        internal reference id for Randori support to track this error  # noqa: E501

        :return: The ref of this ErrorSchema.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ErrorSchema.

        internal reference id for Randori support to track this error  # noqa: E501

        :param ref: The ref of this ErrorSchema.  # noqa: E501
        :type: str
        """

        self._ref = ref

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
