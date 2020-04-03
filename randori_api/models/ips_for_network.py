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


class IpsForNetwork(object):
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
        'affiliation_state': 'str',
        'confidence': 'int',
        'country': 'str',
        'deleted': 'bool',
        'first_seen': 'str',
        'hostname': 'str',
        'id': 'str',
        'impact_score': 'str',
        'ip': 'str',
        'ip_id': 'str',
        'ip_str': 'str',
        'last_seen': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'max_confidence': 'int',
        'network': 'str',
        'network_id': 'str',
        'network_str': 'str',
        'open_port_count': 'int',
        'org_id': 'str',
        'perspective': 'str',
        'perspective_name': 'str',
        'radius': 'float',
        'refreshed': 'bool',
        'service_count': 'int',
        'status': 'str',
        'tags': 'object',
        'target_count': 'int',
        'target_temptation': 'int'
    }

    attribute_map = {
        'affiliation_state': 'affiliation_state',
        'confidence': 'confidence',
        'country': 'country',
        'deleted': 'deleted',
        'first_seen': 'first_seen',
        'hostname': 'hostname',
        'id': 'id',
        'impact_score': 'impact_score',
        'ip': 'ip',
        'ip_id': 'ip_id',
        'ip_str': 'ip_str',
        'last_seen': 'last_seen',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'max_confidence': 'max_confidence',
        'network': 'network',
        'network_id': 'network_id',
        'network_str': 'network_str',
        'open_port_count': 'open_port_count',
        'org_id': 'org_id',
        'perspective': 'perspective',
        'perspective_name': 'perspective_name',
        'radius': 'radius',
        'refreshed': 'refreshed',
        'service_count': 'service_count',
        'status': 'status',
        'tags': 'tags',
        'target_count': 'target_count',
        'target_temptation': 'target_temptation'
    }

    def __init__(self, affiliation_state=None, confidence=None, country=None, deleted=None, first_seen=None, hostname=None, id=None, impact_score=None, ip=None, ip_id=None, ip_str=None, last_seen=None, latitude=None, longitude=None, max_confidence=None, network=None, network_id=None, network_str=None, open_port_count=None, org_id=None, perspective=None, perspective_name=None, radius=None, refreshed=None, service_count=None, status=None, tags=None, target_count=None, target_temptation=None, local_vars_configuration=None):  # noqa: E501
        """IpsForNetwork - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affiliation_state = None
        self._confidence = None
        self._country = None
        self._deleted = None
        self._first_seen = None
        self._hostname = None
        self._id = None
        self._impact_score = None
        self._ip = None
        self._ip_id = None
        self._ip_str = None
        self._last_seen = None
        self._latitude = None
        self._longitude = None
        self._max_confidence = None
        self._network = None
        self._network_id = None
        self._network_str = None
        self._open_port_count = None
        self._org_id = None
        self._perspective = None
        self._perspective_name = None
        self._radius = None
        self._refreshed = None
        self._service_count = None
        self._status = None
        self._tags = None
        self._target_count = None
        self._target_temptation = None
        self.discriminator = None

        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        self.confidence = confidence
        self.country = country
        if deleted is not None:
            self.deleted = deleted
        if first_seen is not None:
            self.first_seen = first_seen
        self.hostname = hostname
        self.id = id
        if impact_score is not None:
            self.impact_score = impact_score
        self.ip = ip
        self.ip_id = ip_id
        self.ip_str = ip_str
        if last_seen is not None:
            self.last_seen = last_seen
        self.latitude = latitude
        self.longitude = longitude
        self.max_confidence = max_confidence
        self.network = network
        self.network_id = network_id
        self.network_str = network_str
        self.open_port_count = open_port_count
        self.org_id = org_id
        self.perspective = perspective
        self.perspective_name = perspective_name
        self.radius = radius
        if refreshed is not None:
            self.refreshed = refreshed
        self.service_count = service_count
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        self.target_count = target_count
        self.target_temptation = target_temptation

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this IpsForNetwork.  # noqa: E501


        :return: The affiliation_state of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this IpsForNetwork.


        :param affiliation_state: The affiliation_state of this IpsForNetwork.  # noqa: E501
        :type: str
        """
        allowed_values = ["Affiliated", "Unaffiliated", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and affiliation_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `affiliation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(affiliation_state, allowed_values)
            )

        self._affiliation_state = affiliation_state

    @property
    def confidence(self):
        """Gets the confidence of this IpsForNetwork.  # noqa: E501


        :return: The confidence of this IpsForNetwork.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this IpsForNetwork.


        :param confidence: The confidence of this IpsForNetwork.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def country(self):
        """Gets the country of this IpsForNetwork.  # noqa: E501


        :return: The country of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IpsForNetwork.


        :param country: The country of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def deleted(self):
        """Gets the deleted of this IpsForNetwork.  # noqa: E501


        :return: The deleted of this IpsForNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this IpsForNetwork.


        :param deleted: The deleted of this IpsForNetwork.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def first_seen(self):
        """Gets the first_seen of this IpsForNetwork.  # noqa: E501


        :return: The first_seen of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this IpsForNetwork.


        :param first_seen: The first_seen of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._first_seen = first_seen

    @property
    def hostname(self):
        """Gets the hostname of this IpsForNetwork.  # noqa: E501


        :return: The hostname of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this IpsForNetwork.


        :param hostname: The hostname of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this IpsForNetwork.  # noqa: E501


        :return: The id of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpsForNetwork.


        :param id: The id of this IpsForNetwork.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact_score(self):
        """Gets the impact_score of this IpsForNetwork.  # noqa: E501


        :return: The impact_score of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this IpsForNetwork.


        :param impact_score: The impact_score of this IpsForNetwork.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Low", "Medium", "High"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and impact_score not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `impact_score` ({0}), must be one of {1}"  # noqa: E501
                .format(impact_score, allowed_values)
            )

        self._impact_score = impact_score

    @property
    def ip(self):
        """Gets the ip of this IpsForNetwork.  # noqa: E501


        :return: The ip of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpsForNetwork.


        :param ip: The ip of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ip_id(self):
        """Gets the ip_id of this IpsForNetwork.  # noqa: E501


        :return: The ip_id of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this IpsForNetwork.


        :param ip_id: The ip_id of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._ip_id = ip_id

    @property
    def ip_str(self):
        """Gets the ip_str of this IpsForNetwork.  # noqa: E501


        :return: The ip_str of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._ip_str

    @ip_str.setter
    def ip_str(self, ip_str):
        """Sets the ip_str of this IpsForNetwork.


        :param ip_str: The ip_str of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._ip_str = ip_str

    @property
    def last_seen(self):
        """Gets the last_seen of this IpsForNetwork.  # noqa: E501


        :return: The last_seen of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this IpsForNetwork.


        :param last_seen: The last_seen of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._last_seen = last_seen

    @property
    def latitude(self):
        """Gets the latitude of this IpsForNetwork.  # noqa: E501


        :return: The latitude of this IpsForNetwork.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this IpsForNetwork.


        :param latitude: The latitude of this IpsForNetwork.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this IpsForNetwork.  # noqa: E501


        :return: The longitude of this IpsForNetwork.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this IpsForNetwork.


        :param longitude: The longitude of this IpsForNetwork.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def max_confidence(self):
        """Gets the max_confidence of this IpsForNetwork.  # noqa: E501


        :return: The max_confidence of this IpsForNetwork.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this IpsForNetwork.


        :param max_confidence: The max_confidence of this IpsForNetwork.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def network(self):
        """Gets the network of this IpsForNetwork.  # noqa: E501


        :return: The network of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this IpsForNetwork.


        :param network: The network of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def network_id(self):
        """Gets the network_id of this IpsForNetwork.  # noqa: E501


        :return: The network_id of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this IpsForNetwork.


        :param network_id: The network_id of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def network_str(self):
        """Gets the network_str of this IpsForNetwork.  # noqa: E501


        :return: The network_str of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._network_str

    @network_str.setter
    def network_str(self, network_str):
        """Sets the network_str of this IpsForNetwork.


        :param network_str: The network_str of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._network_str = network_str

    @property
    def open_port_count(self):
        """Gets the open_port_count of this IpsForNetwork.  # noqa: E501


        :return: The open_port_count of this IpsForNetwork.  # noqa: E501
        :rtype: int
        """
        return self._open_port_count

    @open_port_count.setter
    def open_port_count(self, open_port_count):
        """Sets the open_port_count of this IpsForNetwork.


        :param open_port_count: The open_port_count of this IpsForNetwork.  # noqa: E501
        :type: int
        """

        self._open_port_count = open_port_count

    @property
    def org_id(self):
        """Gets the org_id of this IpsForNetwork.  # noqa: E501


        :return: The org_id of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this IpsForNetwork.


        :param org_id: The org_id of this IpsForNetwork.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def perspective(self):
        """Gets the perspective of this IpsForNetwork.  # noqa: E501


        :return: The perspective of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this IpsForNetwork.


        :param perspective: The perspective of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._perspective = perspective

    @property
    def perspective_name(self):
        """Gets the perspective_name of this IpsForNetwork.  # noqa: E501


        :return: The perspective_name of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this IpsForNetwork.


        :param perspective_name: The perspective_name of this IpsForNetwork.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def radius(self):
        """Gets the radius of this IpsForNetwork.  # noqa: E501


        :return: The radius of this IpsForNetwork.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this IpsForNetwork.


        :param radius: The radius of this IpsForNetwork.  # noqa: E501
        :type: float
        """

        self._radius = radius

    @property
    def refreshed(self):
        """Gets the refreshed of this IpsForNetwork.  # noqa: E501


        :return: The refreshed of this IpsForNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._refreshed

    @refreshed.setter
    def refreshed(self, refreshed):
        """Sets the refreshed of this IpsForNetwork.


        :param refreshed: The refreshed of this IpsForNetwork.  # noqa: E501
        :type: bool
        """

        self._refreshed = refreshed

    @property
    def service_count(self):
        """Gets the service_count of this IpsForNetwork.  # noqa: E501


        :return: The service_count of this IpsForNetwork.  # noqa: E501
        :rtype: int
        """
        return self._service_count

    @service_count.setter
    def service_count(self, service_count):
        """Sets the service_count of this IpsForNetwork.


        :param service_count: The service_count of this IpsForNetwork.  # noqa: E501
        :type: int
        """

        self._service_count = service_count

    @property
    def status(self):
        """Gets the status of this IpsForNetwork.  # noqa: E501


        :return: The status of this IpsForNetwork.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IpsForNetwork.


        :param status: The status of this IpsForNetwork.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Investigate", "In-progress", "Reviewed", "Resolved"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this IpsForNetwork.  # noqa: E501


        :return: The tags of this IpsForNetwork.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IpsForNetwork.


        :param tags: The tags of this IpsForNetwork.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def target_count(self):
        """Gets the target_count of this IpsForNetwork.  # noqa: E501


        :return: The target_count of this IpsForNetwork.  # noqa: E501
        :rtype: int
        """
        return self._target_count

    @target_count.setter
    def target_count(self, target_count):
        """Sets the target_count of this IpsForNetwork.


        :param target_count: The target_count of this IpsForNetwork.  # noqa: E501
        :type: int
        """

        self._target_count = target_count

    @property
    def target_temptation(self):
        """Gets the target_temptation of this IpsForNetwork.  # noqa: E501


        :return: The target_temptation of this IpsForNetwork.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this IpsForNetwork.


        :param target_temptation: The target_temptation of this IpsForNetwork.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

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
        if not isinstance(other, IpsForNetwork):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpsForNetwork):
            return True

        return self.to_dict() != other.to_dict()
