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


class HostnamesForIp(object):
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
        'confidence': 'int',
        'deleted': 'bool',
        'hostname': 'str',
        'hostname_id': 'str',
        'hostname_tags': 'object',
        'id': 'str',
        'ip_id': 'str',
        'last_seen': 'datetime',
        'max_confidence': 'int',
        'org_id': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'deleted': 'deleted',
        'hostname': 'hostname',
        'hostname_id': 'hostname_id',
        'hostname_tags': 'hostname_tags',
        'id': 'id',
        'ip_id': 'ip_id',
        'last_seen': 'last_seen',
        'max_confidence': 'max_confidence',
        'org_id': 'org_id'
    }

    def __init__(self, confidence=None, deleted=None, hostname=None, hostname_id=None, hostname_tags=None, id=None, ip_id=None, last_seen=None, max_confidence=None, org_id=None):  # noqa: E501
        """HostnamesForIp - a model defined in OpenAPI"""  # noqa: E501

        self._confidence = None
        self._deleted = None
        self._hostname = None
        self._hostname_id = None
        self._hostname_tags = None
        self._id = None
        self._ip_id = None
        self._last_seen = None
        self._max_confidence = None
        self._org_id = None
        self.discriminator = None

        self.confidence = confidence
        if deleted is not None:
            self.deleted = deleted
        self.hostname = hostname
        self.hostname_id = hostname_id
        self.hostname_tags = hostname_tags
        self.id = id
        self.ip_id = ip_id
        self.last_seen = last_seen
        self.max_confidence = max_confidence
        self.org_id = org_id

    @property
    def confidence(self):
        """Gets the confidence of this HostnamesForIp.  # noqa: E501


        :return: The confidence of this HostnamesForIp.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this HostnamesForIp.


        :param confidence: The confidence of this HostnamesForIp.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def deleted(self):
        """Gets the deleted of this HostnamesForIp.  # noqa: E501


        :return: The deleted of this HostnamesForIp.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this HostnamesForIp.


        :param deleted: The deleted of this HostnamesForIp.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def hostname(self):
        """Gets the hostname of this HostnamesForIp.  # noqa: E501


        :return: The hostname of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this HostnamesForIp.


        :param hostname: The hostname of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def hostname_id(self):
        """Gets the hostname_id of this HostnamesForIp.  # noqa: E501


        :return: The hostname_id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._hostname_id

    @hostname_id.setter
    def hostname_id(self, hostname_id):
        """Sets the hostname_id of this HostnamesForIp.


        :param hostname_id: The hostname_id of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._hostname_id = hostname_id

    @property
    def hostname_tags(self):
        """Gets the hostname_tags of this HostnamesForIp.  # noqa: E501


        :return: The hostname_tags of this HostnamesForIp.  # noqa: E501
        :rtype: object
        """
        return self._hostname_tags

    @hostname_tags.setter
    def hostname_tags(self, hostname_tags):
        """Sets the hostname_tags of this HostnamesForIp.


        :param hostname_tags: The hostname_tags of this HostnamesForIp.  # noqa: E501
        :type: object
        """

        self._hostname_tags = hostname_tags

    @property
    def id(self):
        """Gets the id of this HostnamesForIp.  # noqa: E501


        :return: The id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostnamesForIp.


        :param id: The id of this HostnamesForIp.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip_id(self):
        """Gets the ip_id of this HostnamesForIp.  # noqa: E501


        :return: The ip_id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this HostnamesForIp.


        :param ip_id: The ip_id of this HostnamesForIp.  # noqa: E501
        :type: str
        """

        self._ip_id = ip_id

    @property
    def last_seen(self):
        """Gets the last_seen of this HostnamesForIp.  # noqa: E501


        :return: The last_seen of this HostnamesForIp.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this HostnamesForIp.


        :param last_seen: The last_seen of this HostnamesForIp.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def max_confidence(self):
        """Gets the max_confidence of this HostnamesForIp.  # noqa: E501


        :return: The max_confidence of this HostnamesForIp.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this HostnamesForIp.


        :param max_confidence: The max_confidence of this HostnamesForIp.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def org_id(self):
        """Gets the org_id of this HostnamesForIp.  # noqa: E501


        :return: The org_id of this HostnamesForIp.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this HostnamesForIp.


        :param org_id: The org_id of this HostnamesForIp.  # noqa: E501
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

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
        if not isinstance(other, HostnamesForIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
