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


class Statistics(object):
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
        'current': 'bool',
        'id': 'str',
        'index': 'int',
        'latest': 'bool',
        'name': 'str',
        'org_id': 'str',
        'row_time': 'datetime',
        'time': 'datetime',
        'type': 'str',
        'value': 'int'
    }

    attribute_map = {
        'current': 'current',
        'id': 'id',
        'index': 'index',
        'latest': 'latest',
        'name': 'name',
        'org_id': 'org_id',
        'row_time': 'row_time',
        'time': 'time',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, current=None, id=None, index=None, latest=None, name=None, org_id=None, row_time=None, time=None, type=None, value=None):  # noqa: E501
        """Statistics - a model defined in OpenAPI"""  # noqa: E501

        self._current = None
        self._id = None
        self._index = None
        self._latest = None
        self._name = None
        self._org_id = None
        self._row_time = None
        self._time = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.current = current
        if id is not None:
            self.id = id
        self.index = index
        self.latest = latest
        self.name = name
        self.org_id = org_id
        self.row_time = row_time
        self.time = time
        self.type = type
        self.value = value

    @property
    def current(self):
        """Gets the current of this Statistics.  # noqa: E501


        :return: The current of this Statistics.  # noqa: E501
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this Statistics.


        :param current: The current of this Statistics.  # noqa: E501
        :type: bool
        """

        self._current = current

    @property
    def id(self):
        """Gets the id of this Statistics.  # noqa: E501


        :return: The id of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Statistics.


        :param id: The id of this Statistics.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def index(self):
        """Gets the index of this Statistics.  # noqa: E501


        :return: The index of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Statistics.


        :param index: The index of this Statistics.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def latest(self):
        """Gets the latest of this Statistics.  # noqa: E501


        :return: The latest of this Statistics.  # noqa: E501
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this Statistics.


        :param latest: The latest of this Statistics.  # noqa: E501
        :type: bool
        """

        self._latest = latest

    @property
    def name(self):
        """Gets the name of this Statistics.  # noqa: E501


        :return: The name of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Statistics.


        :param name: The name of this Statistics.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this Statistics.  # noqa: E501


        :return: The org_id of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Statistics.


        :param org_id: The org_id of this Statistics.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def row_time(self):
        """Gets the row_time of this Statistics.  # noqa: E501


        :return: The row_time of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._row_time

    @row_time.setter
    def row_time(self, row_time):
        """Sets the row_time of this Statistics.


        :param row_time: The row_time of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._row_time = row_time

    @property
    def time(self):
        """Gets the time of this Statistics.  # noqa: E501


        :return: The time of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Statistics.


        :param time: The time of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def type(self):
        """Gets the type of this Statistics.  # noqa: E501


        :return: The type of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Statistics.


        :param type: The type of this Statistics.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this Statistics.  # noqa: E501


        :return: The value of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Statistics.


        :param value: The value of this Statistics.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
