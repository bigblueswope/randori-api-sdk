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


class IpsForHostname(object):
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
        'country': 'str',
        'deleted': 'bool',
        'hostname_id': 'str',
        'id': 'str',
        'ip': 'str',
        'ip_id': 'str',
        'ip_str': 'str',
        'ip_tags': 'object',
        'last_seen': 'datetime',
        'latitude': 'float',
        'longitude': 'float',
        'max_confidence': 'int',
        'open_port_count': 'int',
        'org_id': 'str',
        'radius': 'float',
        'service_count': 'int',
        'target_count': 'int',
        'target_temptation': 'int',
        'top_hostname': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'country': 'country',
        'deleted': 'deleted',
        'hostname_id': 'hostname_id',
        'id': 'id',
        'ip': 'ip',
        'ip_id': 'ip_id',
        'ip_str': 'ip_str',
        'ip_tags': 'ip_tags',
        'last_seen': 'last_seen',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'max_confidence': 'max_confidence',
        'open_port_count': 'open_port_count',
        'org_id': 'org_id',
        'radius': 'radius',
        'service_count': 'service_count',
        'target_count': 'target_count',
        'target_temptation': 'target_temptation',
        'top_hostname': 'top_hostname'
    }

    def __init__(self, confidence=None, country=None, deleted=None, hostname_id=None, id=None, ip=None, ip_id=None, ip_str=None, ip_tags=None, last_seen=None, latitude=None, longitude=None, max_confidence=None, open_port_count=None, org_id=None, radius=None, service_count=None, target_count=None, target_temptation=None, top_hostname=None, local_vars_configuration=None):  # noqa: E501
        """IpsForHostname - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._confidence = None
        self._country = None
        self._deleted = None
        self._hostname_id = None
        self._id = None
        self._ip = None
        self._ip_id = None
        self._ip_str = None
        self._ip_tags = None
        self._last_seen = None
        self._latitude = None
        self._longitude = None
        self._max_confidence = None
        self._open_port_count = None
        self._org_id = None
        self._radius = None
        self._service_count = None
        self._target_count = None
        self._target_temptation = None
        self._top_hostname = None
        self.discriminator = None

        self.confidence = confidence
        self.country = country
        if deleted is not None:
            self.deleted = deleted
        self.hostname_id = hostname_id
        self.id = id
        self.ip = ip
        self.ip_id = ip_id
        self.ip_str = ip_str
        self.ip_tags = ip_tags
        self.last_seen = last_seen
        self.latitude = latitude
        self.longitude = longitude
        self.max_confidence = max_confidence
        self.open_port_count = open_port_count
        self.org_id = org_id
        self.radius = radius
        self.service_count = service_count
        self.target_count = target_count
        self.target_temptation = target_temptation
        self.top_hostname = top_hostname

    @property
    def confidence(self):
        """Gets the confidence of this IpsForHostname.  # noqa: E501


        :return: The confidence of this IpsForHostname.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this IpsForHostname.


        :param confidence: The confidence of this IpsForHostname.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def country(self):
        """Gets the country of this IpsForHostname.  # noqa: E501


        :return: The country of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IpsForHostname.


        :param country: The country of this IpsForHostname.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def deleted(self):
        """Gets the deleted of this IpsForHostname.  # noqa: E501


        :return: The deleted of this IpsForHostname.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this IpsForHostname.


        :param deleted: The deleted of this IpsForHostname.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def hostname_id(self):
        """Gets the hostname_id of this IpsForHostname.  # noqa: E501


        :return: The hostname_id of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._hostname_id

    @hostname_id.setter
    def hostname_id(self, hostname_id):
        """Sets the hostname_id of this IpsForHostname.


        :param hostname_id: The hostname_id of this IpsForHostname.  # noqa: E501
        :type: str
        """

        self._hostname_id = hostname_id

    @property
    def id(self):
        """Gets the id of this IpsForHostname.  # noqa: E501


        :return: The id of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpsForHostname.


        :param id: The id of this IpsForHostname.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this IpsForHostname.  # noqa: E501


        :return: The ip of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpsForHostname.


        :param ip: The ip of this IpsForHostname.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ip_id(self):
        """Gets the ip_id of this IpsForHostname.  # noqa: E501


        :return: The ip_id of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this IpsForHostname.


        :param ip_id: The ip_id of this IpsForHostname.  # noqa: E501
        :type: str
        """

        self._ip_id = ip_id

    @property
    def ip_str(self):
        """Gets the ip_str of this IpsForHostname.  # noqa: E501


        :return: The ip_str of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._ip_str

    @ip_str.setter
    def ip_str(self, ip_str):
        """Sets the ip_str of this IpsForHostname.


        :param ip_str: The ip_str of this IpsForHostname.  # noqa: E501
        :type: str
        """

        self._ip_str = ip_str

    @property
    def ip_tags(self):
        """Gets the ip_tags of this IpsForHostname.  # noqa: E501


        :return: The ip_tags of this IpsForHostname.  # noqa: E501
        :rtype: object
        """
        return self._ip_tags

    @ip_tags.setter
    def ip_tags(self, ip_tags):
        """Sets the ip_tags of this IpsForHostname.


        :param ip_tags: The ip_tags of this IpsForHostname.  # noqa: E501
        :type: object
        """

        self._ip_tags = ip_tags

    @property
    def last_seen(self):
        """Gets the last_seen of this IpsForHostname.  # noqa: E501


        :return: The last_seen of this IpsForHostname.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this IpsForHostname.


        :param last_seen: The last_seen of this IpsForHostname.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def latitude(self):
        """Gets the latitude of this IpsForHostname.  # noqa: E501


        :return: The latitude of this IpsForHostname.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this IpsForHostname.


        :param latitude: The latitude of this IpsForHostname.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this IpsForHostname.  # noqa: E501


        :return: The longitude of this IpsForHostname.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this IpsForHostname.


        :param longitude: The longitude of this IpsForHostname.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def max_confidence(self):
        """Gets the max_confidence of this IpsForHostname.  # noqa: E501


        :return: The max_confidence of this IpsForHostname.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this IpsForHostname.


        :param max_confidence: The max_confidence of this IpsForHostname.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def open_port_count(self):
        """Gets the open_port_count of this IpsForHostname.  # noqa: E501


        :return: The open_port_count of this IpsForHostname.  # noqa: E501
        :rtype: int
        """
        return self._open_port_count

    @open_port_count.setter
    def open_port_count(self, open_port_count):
        """Sets the open_port_count of this IpsForHostname.


        :param open_port_count: The open_port_count of this IpsForHostname.  # noqa: E501
        :type: int
        """

        self._open_port_count = open_port_count

    @property
    def org_id(self):
        """Gets the org_id of this IpsForHostname.  # noqa: E501


        :return: The org_id of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this IpsForHostname.


        :param org_id: The org_id of this IpsForHostname.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def radius(self):
        """Gets the radius of this IpsForHostname.  # noqa: E501


        :return: The radius of this IpsForHostname.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this IpsForHostname.


        :param radius: The radius of this IpsForHostname.  # noqa: E501
        :type: float
        """

        self._radius = radius

    @property
    def service_count(self):
        """Gets the service_count of this IpsForHostname.  # noqa: E501


        :return: The service_count of this IpsForHostname.  # noqa: E501
        :rtype: int
        """
        return self._service_count

    @service_count.setter
    def service_count(self, service_count):
        """Sets the service_count of this IpsForHostname.


        :param service_count: The service_count of this IpsForHostname.  # noqa: E501
        :type: int
        """

        self._service_count = service_count

    @property
    def target_count(self):
        """Gets the target_count of this IpsForHostname.  # noqa: E501


        :return: The target_count of this IpsForHostname.  # noqa: E501
        :rtype: int
        """
        return self._target_count

    @target_count.setter
    def target_count(self, target_count):
        """Sets the target_count of this IpsForHostname.


        :param target_count: The target_count of this IpsForHostname.  # noqa: E501
        :type: int
        """

        self._target_count = target_count

    @property
    def target_temptation(self):
        """Gets the target_temptation of this IpsForHostname.  # noqa: E501


        :return: The target_temptation of this IpsForHostname.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this IpsForHostname.


        :param target_temptation: The target_temptation of this IpsForHostname.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

    @property
    def top_hostname(self):
        """Gets the top_hostname of this IpsForHostname.  # noqa: E501


        :return: The top_hostname of this IpsForHostname.  # noqa: E501
        :rtype: str
        """
        return self._top_hostname

    @top_hostname.setter
    def top_hostname(self, top_hostname):
        """Sets the top_hostname of this IpsForHostname.


        :param top_hostname: The top_hostname of this IpsForHostname.  # noqa: E501
        :type: str
        """

        self._top_hostname = top_hostname

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
        if not isinstance(other, IpsForHostname):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpsForHostname):
            return True

        return self.to_dict() != other.to_dict()
