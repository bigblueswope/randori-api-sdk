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

from randori_api.configuration import Configuration


class PriorityGroupOuterResult(object):
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
        'prio_counts': 'list[PriorityGroupInnerResult]',
        'total_in_ranges': 'int',
        'total_other': 'int'
    }

    attribute_map = {
        'prio_counts': 'prio_counts',
        'total_in_ranges': 'total_in_ranges',
        'total_other': 'total_other'
    }

    def __init__(self, prio_counts=None, total_in_ranges=None, total_other=None, local_vars_configuration=None):  # noqa: E501
        """PriorityGroupOuterResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prio_counts = None
        self._total_in_ranges = None
        self._total_other = None
        self.discriminator = None

        if prio_counts is not None:
            self.prio_counts = prio_counts
        if total_in_ranges is not None:
            self.total_in_ranges = total_in_ranges
        if total_other is not None:
            self.total_other = total_other

    @property
    def prio_counts(self):
        """Gets the prio_counts of this PriorityGroupOuterResult.  # noqa: E501


        :return: The prio_counts of this PriorityGroupOuterResult.  # noqa: E501
        :rtype: list[PriorityGroupInnerResult]
        """
        return self._prio_counts

    @prio_counts.setter
    def prio_counts(self, prio_counts):
        """Sets the prio_counts of this PriorityGroupOuterResult.


        :param prio_counts: The prio_counts of this PriorityGroupOuterResult.  # noqa: E501
        :type: list[PriorityGroupInnerResult]
        """

        self._prio_counts = prio_counts

    @property
    def total_in_ranges(self):
        """Gets the total_in_ranges of this PriorityGroupOuterResult.  # noqa: E501


        :return: The total_in_ranges of this PriorityGroupOuterResult.  # noqa: E501
        :rtype: int
        """
        return self._total_in_ranges

    @total_in_ranges.setter
    def total_in_ranges(self, total_in_ranges):
        """Sets the total_in_ranges of this PriorityGroupOuterResult.


        :param total_in_ranges: The total_in_ranges of this PriorityGroupOuterResult.  # noqa: E501
        :type: int
        """

        self._total_in_ranges = total_in_ranges

    @property
    def total_other(self):
        """Gets the total_other of this PriorityGroupOuterResult.  # noqa: E501


        :return: The total_other of this PriorityGroupOuterResult.  # noqa: E501
        :rtype: int
        """
        return self._total_other

    @total_other.setter
    def total_other(self, total_other):
        """Sets the total_other of this PriorityGroupOuterResult.


        :param total_other: The total_other of this PriorityGroupOuterResult.  # noqa: E501
        :type: int
        """

        self._total_other = total_other

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
        if not isinstance(other, PriorityGroupOuterResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriorityGroupOuterResult):
            return True

        return self.to_dict() != other.to_dict()