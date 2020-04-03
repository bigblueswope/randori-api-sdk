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


class Target(object):
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
        'applicability': 'int',
        'authorization_state': 'str',
        'banner_uuid': 'str',
        'cert_uuid': 'str',
        'confidence': 'int',
        'criticality': 'int',
        'deleted': 'bool',
        'description': 'str',
        'detection_criteria': 'object',
        'enumerability': 'int',
        'first_seen': 'str',
        'headers_uuid': 'str',
        'hostname': 'str',
        'hostname_id': 'str',
        'id': 'str',
        'impact_score': 'str',
        'ip': 'str',
        'ip_id': 'str',
        'ip_str': 'str',
        'last_seen': 'str',
        'max_confidence': 'int',
        'name': 'str',
        'org_id': 'str',
        'path': 'str',
        'perspective': 'str',
        'perspective_name': 'str',
        'port': 'int',
        'post_exploit': 'int',
        'private_weakness': 'int',
        'protocol': 'str',
        'public_weakness': 'int',
        'randori_notes': 'str',
        'reference': 'str',
        'refreshed': 'bool',
        'research': 'int',
        'screenshot_uuid': 'str',
        'service_id': 'str',
        'status': 'str',
        'tags': 'object',
        'target_temptation': 'int',
        'thumbnail_uuid': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'affiliation_state': 'affiliation_state',
        'applicability': 'applicability',
        'authorization_state': 'authorization_state',
        'banner_uuid': 'banner_uuid',
        'cert_uuid': 'cert_uuid',
        'confidence': 'confidence',
        'criticality': 'criticality',
        'deleted': 'deleted',
        'description': 'description',
        'detection_criteria': 'detection_criteria',
        'enumerability': 'enumerability',
        'first_seen': 'first_seen',
        'headers_uuid': 'headers_uuid',
        'hostname': 'hostname',
        'hostname_id': 'hostname_id',
        'id': 'id',
        'impact_score': 'impact_score',
        'ip': 'ip',
        'ip_id': 'ip_id',
        'ip_str': 'ip_str',
        'last_seen': 'last_seen',
        'max_confidence': 'max_confidence',
        'name': 'name',
        'org_id': 'org_id',
        'path': 'path',
        'perspective': 'perspective',
        'perspective_name': 'perspective_name',
        'port': 'port',
        'post_exploit': 'post_exploit',
        'private_weakness': 'private_weakness',
        'protocol': 'protocol',
        'public_weakness': 'public_weakness',
        'randori_notes': 'randori_notes',
        'reference': 'reference',
        'refreshed': 'refreshed',
        'research': 'research',
        'screenshot_uuid': 'screenshot_uuid',
        'service_id': 'service_id',
        'status': 'status',
        'tags': 'tags',
        'target_temptation': 'target_temptation',
        'thumbnail_uuid': 'thumbnail_uuid',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, affiliation_state=None, applicability=None, authorization_state=None, banner_uuid=None, cert_uuid=None, confidence=None, criticality=None, deleted=None, description=None, detection_criteria=None, enumerability=None, first_seen=None, headers_uuid=None, hostname=None, hostname_id=None, id=None, impact_score=None, ip=None, ip_id=None, ip_str=None, last_seen=None, max_confidence=None, name=None, org_id=None, path=None, perspective=None, perspective_name=None, port=None, post_exploit=None, private_weakness=None, protocol=None, public_weakness=None, randori_notes=None, reference=None, refreshed=None, research=None, screenshot_uuid=None, service_id=None, status=None, tags=None, target_temptation=None, thumbnail_uuid=None, vendor=None, version=None, local_vars_configuration=None):  # noqa: E501
        """Target - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affiliation_state = None
        self._applicability = None
        self._authorization_state = None
        self._banner_uuid = None
        self._cert_uuid = None
        self._confidence = None
        self._criticality = None
        self._deleted = None
        self._description = None
        self._detection_criteria = None
        self._enumerability = None
        self._first_seen = None
        self._headers_uuid = None
        self._hostname = None
        self._hostname_id = None
        self._id = None
        self._impact_score = None
        self._ip = None
        self._ip_id = None
        self._ip_str = None
        self._last_seen = None
        self._max_confidence = None
        self._name = None
        self._org_id = None
        self._path = None
        self._perspective = None
        self._perspective_name = None
        self._port = None
        self._post_exploit = None
        self._private_weakness = None
        self._protocol = None
        self._public_weakness = None
        self._randori_notes = None
        self._reference = None
        self._refreshed = None
        self._research = None
        self._screenshot_uuid = None
        self._service_id = None
        self._status = None
        self._tags = None
        self._target_temptation = None
        self._thumbnail_uuid = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        if affiliation_state is not None:
            self.affiliation_state = affiliation_state
        self.applicability = applicability
        if authorization_state is not None:
            self.authorization_state = authorization_state
        self.banner_uuid = banner_uuid
        self.cert_uuid = cert_uuid
        self.confidence = confidence
        self.criticality = criticality
        if deleted is not None:
            self.deleted = deleted
        self.description = description
        self.detection_criteria = detection_criteria
        self.enumerability = enumerability
        if first_seen is not None:
            self.first_seen = first_seen
        self.headers_uuid = headers_uuid
        self.hostname = hostname
        self.hostname_id = hostname_id
        self.id = id
        if impact_score is not None:
            self.impact_score = impact_score
        self.ip = ip
        self.ip_id = ip_id
        self.ip_str = ip_str
        if last_seen is not None:
            self.last_seen = last_seen
        self.max_confidence = max_confidence
        self.name = name
        self.org_id = org_id
        self.path = path
        self.perspective = perspective
        self.perspective_name = perspective_name
        self.port = port
        self.post_exploit = post_exploit
        self.private_weakness = private_weakness
        self.protocol = protocol
        self.public_weakness = public_weakness
        self.randori_notes = randori_notes
        self.reference = reference
        if refreshed is not None:
            self.refreshed = refreshed
        self.research = research
        self.screenshot_uuid = screenshot_uuid
        self.service_id = service_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        self.target_temptation = target_temptation
        self.thumbnail_uuid = thumbnail_uuid
        self.vendor = vendor
        self.version = version

    @property
    def affiliation_state(self):
        """Gets the affiliation_state of this Target.  # noqa: E501


        :return: The affiliation_state of this Target.  # noqa: E501
        :rtype: str
        """
        return self._affiliation_state

    @affiliation_state.setter
    def affiliation_state(self, affiliation_state):
        """Sets the affiliation_state of this Target.


        :param affiliation_state: The affiliation_state of this Target.  # noqa: E501
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
    def applicability(self):
        """Gets the applicability of this Target.  # noqa: E501


        :return: The applicability of this Target.  # noqa: E501
        :rtype: int
        """
        return self._applicability

    @applicability.setter
    def applicability(self, applicability):
        """Sets the applicability of this Target.


        :param applicability: The applicability of this Target.  # noqa: E501
        :type: int
        """

        self._applicability = applicability

    @property
    def authorization_state(self):
        """Gets the authorization_state of this Target.  # noqa: E501


        :return: The authorization_state of this Target.  # noqa: E501
        :rtype: str
        """
        return self._authorization_state

    @authorization_state.setter
    def authorization_state(self, authorization_state):
        """Sets the authorization_state of this Target.


        :param authorization_state: The authorization_state of this Target.  # noqa: E501
        :type: str
        """
        allowed_values = ["Authorized", "Prohibited", "None"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and authorization_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `authorization_state` ({0}), must be one of {1}"  # noqa: E501
                .format(authorization_state, allowed_values)
            )

        self._authorization_state = authorization_state

    @property
    def banner_uuid(self):
        """Gets the banner_uuid of this Target.  # noqa: E501


        :return: The banner_uuid of this Target.  # noqa: E501
        :rtype: str
        """
        return self._banner_uuid

    @banner_uuid.setter
    def banner_uuid(self, banner_uuid):
        """Sets the banner_uuid of this Target.


        :param banner_uuid: The banner_uuid of this Target.  # noqa: E501
        :type: str
        """

        self._banner_uuid = banner_uuid

    @property
    def cert_uuid(self):
        """Gets the cert_uuid of this Target.  # noqa: E501


        :return: The cert_uuid of this Target.  # noqa: E501
        :rtype: str
        """
        return self._cert_uuid

    @cert_uuid.setter
    def cert_uuid(self, cert_uuid):
        """Sets the cert_uuid of this Target.


        :param cert_uuid: The cert_uuid of this Target.  # noqa: E501
        :type: str
        """

        self._cert_uuid = cert_uuid

    @property
    def confidence(self):
        """Gets the confidence of this Target.  # noqa: E501


        :return: The confidence of this Target.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this Target.


        :param confidence: The confidence of this Target.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def criticality(self):
        """Gets the criticality of this Target.  # noqa: E501


        :return: The criticality of this Target.  # noqa: E501
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this Target.


        :param criticality: The criticality of this Target.  # noqa: E501
        :type: int
        """

        self._criticality = criticality

    @property
    def deleted(self):
        """Gets the deleted of this Target.  # noqa: E501


        :return: The deleted of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Target.


        :param deleted: The deleted of this Target.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this Target.  # noqa: E501


        :return: The description of this Target.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Target.


        :param description: The description of this Target.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def detection_criteria(self):
        """Gets the detection_criteria of this Target.  # noqa: E501


        :return: The detection_criteria of this Target.  # noqa: E501
        :rtype: object
        """
        return self._detection_criteria

    @detection_criteria.setter
    def detection_criteria(self, detection_criteria):
        """Sets the detection_criteria of this Target.


        :param detection_criteria: The detection_criteria of this Target.  # noqa: E501
        :type: object
        """

        self._detection_criteria = detection_criteria

    @property
    def enumerability(self):
        """Gets the enumerability of this Target.  # noqa: E501


        :return: The enumerability of this Target.  # noqa: E501
        :rtype: int
        """
        return self._enumerability

    @enumerability.setter
    def enumerability(self, enumerability):
        """Sets the enumerability of this Target.


        :param enumerability: The enumerability of this Target.  # noqa: E501
        :type: int
        """

        self._enumerability = enumerability

    @property
    def first_seen(self):
        """Gets the first_seen of this Target.  # noqa: E501


        :return: The first_seen of this Target.  # noqa: E501
        :rtype: str
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this Target.


        :param first_seen: The first_seen of this Target.  # noqa: E501
        :type: str
        """

        self._first_seen = first_seen

    @property
    def headers_uuid(self):
        """Gets the headers_uuid of this Target.  # noqa: E501


        :return: The headers_uuid of this Target.  # noqa: E501
        :rtype: str
        """
        return self._headers_uuid

    @headers_uuid.setter
    def headers_uuid(self, headers_uuid):
        """Sets the headers_uuid of this Target.


        :param headers_uuid: The headers_uuid of this Target.  # noqa: E501
        :type: str
        """

        self._headers_uuid = headers_uuid

    @property
    def hostname(self):
        """Gets the hostname of this Target.  # noqa: E501


        :return: The hostname of this Target.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Target.


        :param hostname: The hostname of this Target.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def hostname_id(self):
        """Gets the hostname_id of this Target.  # noqa: E501


        :return: The hostname_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._hostname_id

    @hostname_id.setter
    def hostname_id(self, hostname_id):
        """Sets the hostname_id of this Target.


        :param hostname_id: The hostname_id of this Target.  # noqa: E501
        :type: str
        """

        self._hostname_id = hostname_id

    @property
    def id(self):
        """Gets the id of this Target.  # noqa: E501


        :return: The id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Target.


        :param id: The id of this Target.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact_score(self):
        """Gets the impact_score of this Target.  # noqa: E501


        :return: The impact_score of this Target.  # noqa: E501
        :rtype: str
        """
        return self._impact_score

    @impact_score.setter
    def impact_score(self, impact_score):
        """Sets the impact_score of this Target.


        :param impact_score: The impact_score of this Target.  # noqa: E501
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
        """Gets the ip of this Target.  # noqa: E501


        :return: The ip of this Target.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Target.


        :param ip: The ip of this Target.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ip_id(self):
        """Gets the ip_id of this Target.  # noqa: E501


        :return: The ip_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this Target.


        :param ip_id: The ip_id of this Target.  # noqa: E501
        :type: str
        """

        self._ip_id = ip_id

    @property
    def ip_str(self):
        """Gets the ip_str of this Target.  # noqa: E501


        :return: The ip_str of this Target.  # noqa: E501
        :rtype: str
        """
        return self._ip_str

    @ip_str.setter
    def ip_str(self, ip_str):
        """Sets the ip_str of this Target.


        :param ip_str: The ip_str of this Target.  # noqa: E501
        :type: str
        """

        self._ip_str = ip_str

    @property
    def last_seen(self):
        """Gets the last_seen of this Target.  # noqa: E501


        :return: The last_seen of this Target.  # noqa: E501
        :rtype: str
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this Target.


        :param last_seen: The last_seen of this Target.  # noqa: E501
        :type: str
        """

        self._last_seen = last_seen

    @property
    def max_confidence(self):
        """Gets the max_confidence of this Target.  # noqa: E501


        :return: The max_confidence of this Target.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this Target.


        :param max_confidence: The max_confidence of this Target.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def name(self):
        """Gets the name of this Target.  # noqa: E501


        :return: The name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Target.


        :param name: The name of this Target.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this Target.  # noqa: E501


        :return: The org_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Target.


        :param org_id: The org_id of this Target.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def path(self):
        """Gets the path of this Target.  # noqa: E501


        :return: The path of this Target.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Target.


        :param path: The path of this Target.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def perspective(self):
        """Gets the perspective of this Target.  # noqa: E501


        :return: The perspective of this Target.  # noqa: E501
        :rtype: str
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this Target.


        :param perspective: The perspective of this Target.  # noqa: E501
        :type: str
        """

        self._perspective = perspective

    @property
    def perspective_name(self):
        """Gets the perspective_name of this Target.  # noqa: E501


        :return: The perspective_name of this Target.  # noqa: E501
        :rtype: str
        """
        return self._perspective_name

    @perspective_name.setter
    def perspective_name(self, perspective_name):
        """Sets the perspective_name of this Target.


        :param perspective_name: The perspective_name of this Target.  # noqa: E501
        :type: str
        """

        self._perspective_name = perspective_name

    @property
    def port(self):
        """Gets the port of this Target.  # noqa: E501


        :return: The port of this Target.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Target.


        :param port: The port of this Target.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def post_exploit(self):
        """Gets the post_exploit of this Target.  # noqa: E501


        :return: The post_exploit of this Target.  # noqa: E501
        :rtype: int
        """
        return self._post_exploit

    @post_exploit.setter
    def post_exploit(self, post_exploit):
        """Sets the post_exploit of this Target.


        :param post_exploit: The post_exploit of this Target.  # noqa: E501
        :type: int
        """

        self._post_exploit = post_exploit

    @property
    def private_weakness(self):
        """Gets the private_weakness of this Target.  # noqa: E501


        :return: The private_weakness of this Target.  # noqa: E501
        :rtype: int
        """
        return self._private_weakness

    @private_weakness.setter
    def private_weakness(self, private_weakness):
        """Sets the private_weakness of this Target.


        :param private_weakness: The private_weakness of this Target.  # noqa: E501
        :type: int
        """

        self._private_weakness = private_weakness

    @property
    def protocol(self):
        """Gets the protocol of this Target.  # noqa: E501


        :return: The protocol of this Target.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Target.


        :param protocol: The protocol of this Target.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def public_weakness(self):
        """Gets the public_weakness of this Target.  # noqa: E501


        :return: The public_weakness of this Target.  # noqa: E501
        :rtype: int
        """
        return self._public_weakness

    @public_weakness.setter
    def public_weakness(self, public_weakness):
        """Sets the public_weakness of this Target.


        :param public_weakness: The public_weakness of this Target.  # noqa: E501
        :type: int
        """

        self._public_weakness = public_weakness

    @property
    def randori_notes(self):
        """Gets the randori_notes of this Target.  # noqa: E501


        :return: The randori_notes of this Target.  # noqa: E501
        :rtype: str
        """
        return self._randori_notes

    @randori_notes.setter
    def randori_notes(self, randori_notes):
        """Sets the randori_notes of this Target.


        :param randori_notes: The randori_notes of this Target.  # noqa: E501
        :type: str
        """

        self._randori_notes = randori_notes

    @property
    def reference(self):
        """Gets the reference of this Target.  # noqa: E501


        :return: The reference of this Target.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Target.


        :param reference: The reference of this Target.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def refreshed(self):
        """Gets the refreshed of this Target.  # noqa: E501


        :return: The refreshed of this Target.  # noqa: E501
        :rtype: bool
        """
        return self._refreshed

    @refreshed.setter
    def refreshed(self, refreshed):
        """Sets the refreshed of this Target.


        :param refreshed: The refreshed of this Target.  # noqa: E501
        :type: bool
        """

        self._refreshed = refreshed

    @property
    def research(self):
        """Gets the research of this Target.  # noqa: E501


        :return: The research of this Target.  # noqa: E501
        :rtype: int
        """
        return self._research

    @research.setter
    def research(self, research):
        """Sets the research of this Target.


        :param research: The research of this Target.  # noqa: E501
        :type: int
        """

        self._research = research

    @property
    def screenshot_uuid(self):
        """Gets the screenshot_uuid of this Target.  # noqa: E501


        :return: The screenshot_uuid of this Target.  # noqa: E501
        :rtype: str
        """
        return self._screenshot_uuid

    @screenshot_uuid.setter
    def screenshot_uuid(self, screenshot_uuid):
        """Sets the screenshot_uuid of this Target.


        :param screenshot_uuid: The screenshot_uuid of this Target.  # noqa: E501
        :type: str
        """

        self._screenshot_uuid = screenshot_uuid

    @property
    def service_id(self):
        """Gets the service_id of this Target.  # noqa: E501


        :return: The service_id of this Target.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Target.


        :param service_id: The service_id of this Target.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def status(self):
        """Gets the status of this Target.  # noqa: E501


        :return: The status of this Target.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Target.


        :param status: The status of this Target.  # noqa: E501
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
        """Gets the tags of this Target.  # noqa: E501


        :return: The tags of this Target.  # noqa: E501
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Target.


        :param tags: The tags of this Target.  # noqa: E501
        :type: object
        """

        self._tags = tags

    @property
    def target_temptation(self):
        """Gets the target_temptation of this Target.  # noqa: E501


        :return: The target_temptation of this Target.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this Target.


        :param target_temptation: The target_temptation of this Target.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

    @property
    def thumbnail_uuid(self):
        """Gets the thumbnail_uuid of this Target.  # noqa: E501


        :return: The thumbnail_uuid of this Target.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_uuid

    @thumbnail_uuid.setter
    def thumbnail_uuid(self, thumbnail_uuid):
        """Sets the thumbnail_uuid of this Target.


        :param thumbnail_uuid: The thumbnail_uuid of this Target.  # noqa: E501
        :type: str
        """

        self._thumbnail_uuid = thumbnail_uuid

    @property
    def vendor(self):
        """Gets the vendor of this Target.  # noqa: E501


        :return: The vendor of this Target.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Target.


        :param vendor: The vendor of this Target.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this Target.  # noqa: E501


        :return: The version of this Target.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Target.


        :param version: The version of this Target.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, Target):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Target):
            return True

        return self.to_dict() != other.to_dict()
