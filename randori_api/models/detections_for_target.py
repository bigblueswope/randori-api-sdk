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


class DetectionsForTarget(object):
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
        'applicability': 'int',
        'banners_uuid': 'str',
        'cert_uuid': 'str',
        'confidence': 'int',
        'criticality': 'int',
        'deleted': 'bool',
        'description': 'str',
        'detection_criteria': 'object',
        'detection_uuid': 'str',
        'enumerability': 'int',
        'first_seen': 'datetime',
        'headers_uuid': 'str',
        'hostname': 'str',
        'hostname_id': 'str',
        'id': 'str',
        'ip': 'str',
        'ip_id': 'str',
        'ip_str': 'str',
        'last_seen': 'datetime',
        'max_confidence': 'int',
        'name': 'str',
        'org_id': 'str',
        'path': 'str',
        'port': 'int',
        'post_exploit': 'int',
        'private_weakness': 'int',
        'protocol': 'str',
        'public_weakness': 'int',
        'randori_notes': 'str',
        'reference': 'str',
        'research': 'int',
        'screenshot_uuid': 'str',
        'service_id': 'str',
        'target_detection_criteria': 'object',
        'target_first_seen': 'datetime',
        'target_hostname': 'str',
        'target_hostname_id': 'str',
        'target_id': 'str',
        'target_ip': 'str',
        'target_ip_str': 'str',
        'target_last_seen': 'datetime',
        'target_path': 'str',
        'target_port': 'int',
        'target_protocol': 'str',
        'target_temptation': 'int',
        'thumbnail_uuid': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'applicability': 'applicability',
        'banners_uuid': 'banners_uuid',
        'cert_uuid': 'cert_uuid',
        'confidence': 'confidence',
        'criticality': 'criticality',
        'deleted': 'deleted',
        'description': 'description',
        'detection_criteria': 'detection_criteria',
        'detection_uuid': 'detection_uuid',
        'enumerability': 'enumerability',
        'first_seen': 'first_seen',
        'headers_uuid': 'headers_uuid',
        'hostname': 'hostname',
        'hostname_id': 'hostname_id',
        'id': 'id',
        'ip': 'ip',
        'ip_id': 'ip_id',
        'ip_str': 'ip_str',
        'last_seen': 'last_seen',
        'max_confidence': 'max_confidence',
        'name': 'name',
        'org_id': 'org_id',
        'path': 'path',
        'port': 'port',
        'post_exploit': 'post_exploit',
        'private_weakness': 'private_weakness',
        'protocol': 'protocol',
        'public_weakness': 'public_weakness',
        'randori_notes': 'randori_notes',
        'reference': 'reference',
        'research': 'research',
        'screenshot_uuid': 'screenshot_uuid',
        'service_id': 'service_id',
        'target_detection_criteria': 'target_detection_criteria',
        'target_first_seen': 'target_first_seen',
        'target_hostname': 'target_hostname',
        'target_hostname_id': 'target_hostname_id',
        'target_id': 'target_id',
        'target_ip': 'target_ip',
        'target_ip_str': 'target_ip_str',
        'target_last_seen': 'target_last_seen',
        'target_path': 'target_path',
        'target_port': 'target_port',
        'target_protocol': 'target_protocol',
        'target_temptation': 'target_temptation',
        'thumbnail_uuid': 'thumbnail_uuid',
        'vendor': 'vendor',
        'version': 'version'
    }

    def __init__(self, applicability=None, banners_uuid=None, cert_uuid=None, confidence=None, criticality=None, deleted=None, description=None, detection_criteria=None, detection_uuid=None, enumerability=None, first_seen=None, headers_uuid=None, hostname=None, hostname_id=None, id=None, ip=None, ip_id=None, ip_str=None, last_seen=None, max_confidence=None, name=None, org_id=None, path=None, port=None, post_exploit=None, private_weakness=None, protocol=None, public_weakness=None, randori_notes=None, reference=None, research=None, screenshot_uuid=None, service_id=None, target_detection_criteria=None, target_first_seen=None, target_hostname=None, target_hostname_id=None, target_id=None, target_ip=None, target_ip_str=None, target_last_seen=None, target_path=None, target_port=None, target_protocol=None, target_temptation=None, thumbnail_uuid=None, vendor=None, version=None, local_vars_configuration=None):  # noqa: E501
        """DetectionsForTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._applicability = None
        self._banners_uuid = None
        self._cert_uuid = None
        self._confidence = None
        self._criticality = None
        self._deleted = None
        self._description = None
        self._detection_criteria = None
        self._detection_uuid = None
        self._enumerability = None
        self._first_seen = None
        self._headers_uuid = None
        self._hostname = None
        self._hostname_id = None
        self._id = None
        self._ip = None
        self._ip_id = None
        self._ip_str = None
        self._last_seen = None
        self._max_confidence = None
        self._name = None
        self._org_id = None
        self._path = None
        self._port = None
        self._post_exploit = None
        self._private_weakness = None
        self._protocol = None
        self._public_weakness = None
        self._randori_notes = None
        self._reference = None
        self._research = None
        self._screenshot_uuid = None
        self._service_id = None
        self._target_detection_criteria = None
        self._target_first_seen = None
        self._target_hostname = None
        self._target_hostname_id = None
        self._target_id = None
        self._target_ip = None
        self._target_ip_str = None
        self._target_last_seen = None
        self._target_path = None
        self._target_port = None
        self._target_protocol = None
        self._target_temptation = None
        self._thumbnail_uuid = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        self.applicability = applicability
        self.banners_uuid = banners_uuid
        self.cert_uuid = cert_uuid
        self.confidence = confidence
        self.criticality = criticality
        if deleted is not None:
            self.deleted = deleted
        self.description = description
        self.detection_criteria = detection_criteria
        self.detection_uuid = detection_uuid
        self.enumerability = enumerability
        self.first_seen = first_seen
        self.headers_uuid = headers_uuid
        self.hostname = hostname
        self.hostname_id = hostname_id
        self.id = id
        self.ip = ip
        self.ip_id = ip_id
        self.ip_str = ip_str
        self.last_seen = last_seen
        self.max_confidence = max_confidence
        self.name = name
        self.org_id = org_id
        self.path = path
        self.port = port
        self.post_exploit = post_exploit
        self.private_weakness = private_weakness
        self.protocol = protocol
        self.public_weakness = public_weakness
        self.randori_notes = randori_notes
        self.reference = reference
        self.research = research
        self.screenshot_uuid = screenshot_uuid
        self.service_id = service_id
        self.target_detection_criteria = target_detection_criteria
        self.target_first_seen = target_first_seen
        self.target_hostname = target_hostname
        self.target_hostname_id = target_hostname_id
        self.target_id = target_id
        self.target_ip = target_ip
        self.target_ip_str = target_ip_str
        self.target_last_seen = target_last_seen
        self.target_path = target_path
        self.target_port = target_port
        self.target_protocol = target_protocol
        self.target_temptation = target_temptation
        self.thumbnail_uuid = thumbnail_uuid
        self.vendor = vendor
        self.version = version

    @property
    def applicability(self):
        """Gets the applicability of this DetectionsForTarget.  # noqa: E501


        :return: The applicability of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._applicability

    @applicability.setter
    def applicability(self, applicability):
        """Sets the applicability of this DetectionsForTarget.


        :param applicability: The applicability of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._applicability = applicability

    @property
    def banners_uuid(self):
        """Gets the banners_uuid of this DetectionsForTarget.  # noqa: E501


        :return: The banners_uuid of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._banners_uuid

    @banners_uuid.setter
    def banners_uuid(self, banners_uuid):
        """Sets the banners_uuid of this DetectionsForTarget.


        :param banners_uuid: The banners_uuid of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._banners_uuid = banners_uuid

    @property
    def cert_uuid(self):
        """Gets the cert_uuid of this DetectionsForTarget.  # noqa: E501


        :return: The cert_uuid of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._cert_uuid

    @cert_uuid.setter
    def cert_uuid(self, cert_uuid):
        """Sets the cert_uuid of this DetectionsForTarget.


        :param cert_uuid: The cert_uuid of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._cert_uuid = cert_uuid

    @property
    def confidence(self):
        """Gets the confidence of this DetectionsForTarget.  # noqa: E501


        :return: The confidence of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this DetectionsForTarget.


        :param confidence: The confidence of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._confidence = confidence

    @property
    def criticality(self):
        """Gets the criticality of this DetectionsForTarget.  # noqa: E501


        :return: The criticality of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this DetectionsForTarget.


        :param criticality: The criticality of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._criticality = criticality

    @property
    def deleted(self):
        """Gets the deleted of this DetectionsForTarget.  # noqa: E501


        :return: The deleted of this DetectionsForTarget.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DetectionsForTarget.


        :param deleted: The deleted of this DetectionsForTarget.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this DetectionsForTarget.  # noqa: E501


        :return: The description of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DetectionsForTarget.


        :param description: The description of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def detection_criteria(self):
        """Gets the detection_criteria of this DetectionsForTarget.  # noqa: E501


        :return: The detection_criteria of this DetectionsForTarget.  # noqa: E501
        :rtype: object
        """
        return self._detection_criteria

    @detection_criteria.setter
    def detection_criteria(self, detection_criteria):
        """Sets the detection_criteria of this DetectionsForTarget.


        :param detection_criteria: The detection_criteria of this DetectionsForTarget.  # noqa: E501
        :type: object
        """

        self._detection_criteria = detection_criteria

    @property
    def detection_uuid(self):
        """Gets the detection_uuid of this DetectionsForTarget.  # noqa: E501


        :return: The detection_uuid of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._detection_uuid

    @detection_uuid.setter
    def detection_uuid(self, detection_uuid):
        """Sets the detection_uuid of this DetectionsForTarget.


        :param detection_uuid: The detection_uuid of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._detection_uuid = detection_uuid

    @property
    def enumerability(self):
        """Gets the enumerability of this DetectionsForTarget.  # noqa: E501


        :return: The enumerability of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._enumerability

    @enumerability.setter
    def enumerability(self, enumerability):
        """Sets the enumerability of this DetectionsForTarget.


        :param enumerability: The enumerability of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._enumerability = enumerability

    @property
    def first_seen(self):
        """Gets the first_seen of this DetectionsForTarget.  # noqa: E501


        :return: The first_seen of this DetectionsForTarget.  # noqa: E501
        :rtype: datetime
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this DetectionsForTarget.


        :param first_seen: The first_seen of this DetectionsForTarget.  # noqa: E501
        :type: datetime
        """

        self._first_seen = first_seen

    @property
    def headers_uuid(self):
        """Gets the headers_uuid of this DetectionsForTarget.  # noqa: E501


        :return: The headers_uuid of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._headers_uuid

    @headers_uuid.setter
    def headers_uuid(self, headers_uuid):
        """Sets the headers_uuid of this DetectionsForTarget.


        :param headers_uuid: The headers_uuid of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._headers_uuid = headers_uuid

    @property
    def hostname(self):
        """Gets the hostname of this DetectionsForTarget.  # noqa: E501


        :return: The hostname of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DetectionsForTarget.


        :param hostname: The hostname of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def hostname_id(self):
        """Gets the hostname_id of this DetectionsForTarget.  # noqa: E501


        :return: The hostname_id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._hostname_id

    @hostname_id.setter
    def hostname_id(self, hostname_id):
        """Sets the hostname_id of this DetectionsForTarget.


        :param hostname_id: The hostname_id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._hostname_id = hostname_id

    @property
    def id(self):
        """Gets the id of this DetectionsForTarget.  # noqa: E501


        :return: The id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DetectionsForTarget.


        :param id: The id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this DetectionsForTarget.  # noqa: E501


        :return: The ip of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DetectionsForTarget.


        :param ip: The ip of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ip_id(self):
        """Gets the ip_id of this DetectionsForTarget.  # noqa: E501


        :return: The ip_id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this DetectionsForTarget.


        :param ip_id: The ip_id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._ip_id = ip_id

    @property
    def ip_str(self):
        """Gets the ip_str of this DetectionsForTarget.  # noqa: E501


        :return: The ip_str of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._ip_str

    @ip_str.setter
    def ip_str(self, ip_str):
        """Sets the ip_str of this DetectionsForTarget.


        :param ip_str: The ip_str of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._ip_str = ip_str

    @property
    def last_seen(self):
        """Gets the last_seen of this DetectionsForTarget.  # noqa: E501


        :return: The last_seen of this DetectionsForTarget.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this DetectionsForTarget.


        :param last_seen: The last_seen of this DetectionsForTarget.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def max_confidence(self):
        """Gets the max_confidence of this DetectionsForTarget.  # noqa: E501


        :return: The max_confidence of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this DetectionsForTarget.


        :param max_confidence: The max_confidence of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._max_confidence = max_confidence

    @property
    def name(self):
        """Gets the name of this DetectionsForTarget.  # noqa: E501


        :return: The name of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetectionsForTarget.


        :param name: The name of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this DetectionsForTarget.  # noqa: E501


        :return: The org_id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this DetectionsForTarget.


        :param org_id: The org_id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def path(self):
        """Gets the path of this DetectionsForTarget.  # noqa: E501


        :return: The path of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DetectionsForTarget.


        :param path: The path of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def port(self):
        """Gets the port of this DetectionsForTarget.  # noqa: E501


        :return: The port of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DetectionsForTarget.


        :param port: The port of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def post_exploit(self):
        """Gets the post_exploit of this DetectionsForTarget.  # noqa: E501


        :return: The post_exploit of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._post_exploit

    @post_exploit.setter
    def post_exploit(self, post_exploit):
        """Sets the post_exploit of this DetectionsForTarget.


        :param post_exploit: The post_exploit of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._post_exploit = post_exploit

    @property
    def private_weakness(self):
        """Gets the private_weakness of this DetectionsForTarget.  # noqa: E501


        :return: The private_weakness of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._private_weakness

    @private_weakness.setter
    def private_weakness(self, private_weakness):
        """Sets the private_weakness of this DetectionsForTarget.


        :param private_weakness: The private_weakness of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._private_weakness = private_weakness

    @property
    def protocol(self):
        """Gets the protocol of this DetectionsForTarget.  # noqa: E501


        :return: The protocol of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DetectionsForTarget.


        :param protocol: The protocol of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def public_weakness(self):
        """Gets the public_weakness of this DetectionsForTarget.  # noqa: E501


        :return: The public_weakness of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._public_weakness

    @public_weakness.setter
    def public_weakness(self, public_weakness):
        """Sets the public_weakness of this DetectionsForTarget.


        :param public_weakness: The public_weakness of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._public_weakness = public_weakness

    @property
    def randori_notes(self):
        """Gets the randori_notes of this DetectionsForTarget.  # noqa: E501


        :return: The randori_notes of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._randori_notes

    @randori_notes.setter
    def randori_notes(self, randori_notes):
        """Sets the randori_notes of this DetectionsForTarget.


        :param randori_notes: The randori_notes of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._randori_notes = randori_notes

    @property
    def reference(self):
        """Gets the reference of this DetectionsForTarget.  # noqa: E501


        :return: The reference of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DetectionsForTarget.


        :param reference: The reference of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def research(self):
        """Gets the research of this DetectionsForTarget.  # noqa: E501


        :return: The research of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._research

    @research.setter
    def research(self, research):
        """Sets the research of this DetectionsForTarget.


        :param research: The research of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._research = research

    @property
    def screenshot_uuid(self):
        """Gets the screenshot_uuid of this DetectionsForTarget.  # noqa: E501


        :return: The screenshot_uuid of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._screenshot_uuid

    @screenshot_uuid.setter
    def screenshot_uuid(self, screenshot_uuid):
        """Sets the screenshot_uuid of this DetectionsForTarget.


        :param screenshot_uuid: The screenshot_uuid of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._screenshot_uuid = screenshot_uuid

    @property
    def service_id(self):
        """Gets the service_id of this DetectionsForTarget.  # noqa: E501


        :return: The service_id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this DetectionsForTarget.


        :param service_id: The service_id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def target_detection_criteria(self):
        """Gets the target_detection_criteria of this DetectionsForTarget.  # noqa: E501


        :return: The target_detection_criteria of this DetectionsForTarget.  # noqa: E501
        :rtype: object
        """
        return self._target_detection_criteria

    @target_detection_criteria.setter
    def target_detection_criteria(self, target_detection_criteria):
        """Sets the target_detection_criteria of this DetectionsForTarget.


        :param target_detection_criteria: The target_detection_criteria of this DetectionsForTarget.  # noqa: E501
        :type: object
        """

        self._target_detection_criteria = target_detection_criteria

    @property
    def target_first_seen(self):
        """Gets the target_first_seen of this DetectionsForTarget.  # noqa: E501


        :return: The target_first_seen of this DetectionsForTarget.  # noqa: E501
        :rtype: datetime
        """
        return self._target_first_seen

    @target_first_seen.setter
    def target_first_seen(self, target_first_seen):
        """Sets the target_first_seen of this DetectionsForTarget.


        :param target_first_seen: The target_first_seen of this DetectionsForTarget.  # noqa: E501
        :type: datetime
        """

        self._target_first_seen = target_first_seen

    @property
    def target_hostname(self):
        """Gets the target_hostname of this DetectionsForTarget.  # noqa: E501


        :return: The target_hostname of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_hostname

    @target_hostname.setter
    def target_hostname(self, target_hostname):
        """Sets the target_hostname of this DetectionsForTarget.


        :param target_hostname: The target_hostname of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_hostname = target_hostname

    @property
    def target_hostname_id(self):
        """Gets the target_hostname_id of this DetectionsForTarget.  # noqa: E501


        :return: The target_hostname_id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_hostname_id

    @target_hostname_id.setter
    def target_hostname_id(self, target_hostname_id):
        """Sets the target_hostname_id of this DetectionsForTarget.


        :param target_hostname_id: The target_hostname_id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_hostname_id = target_hostname_id

    @property
    def target_id(self):
        """Gets the target_id of this DetectionsForTarget.  # noqa: E501


        :return: The target_id of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this DetectionsForTarget.


        :param target_id: The target_id of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def target_ip(self):
        """Gets the target_ip of this DetectionsForTarget.  # noqa: E501


        :return: The target_ip of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """Sets the target_ip of this DetectionsForTarget.


        :param target_ip: The target_ip of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_ip = target_ip

    @property
    def target_ip_str(self):
        """Gets the target_ip_str of this DetectionsForTarget.  # noqa: E501


        :return: The target_ip_str of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_ip_str

    @target_ip_str.setter
    def target_ip_str(self, target_ip_str):
        """Sets the target_ip_str of this DetectionsForTarget.


        :param target_ip_str: The target_ip_str of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_ip_str = target_ip_str

    @property
    def target_last_seen(self):
        """Gets the target_last_seen of this DetectionsForTarget.  # noqa: E501


        :return: The target_last_seen of this DetectionsForTarget.  # noqa: E501
        :rtype: datetime
        """
        return self._target_last_seen

    @target_last_seen.setter
    def target_last_seen(self, target_last_seen):
        """Sets the target_last_seen of this DetectionsForTarget.


        :param target_last_seen: The target_last_seen of this DetectionsForTarget.  # noqa: E501
        :type: datetime
        """

        self._target_last_seen = target_last_seen

    @property
    def target_path(self):
        """Gets the target_path of this DetectionsForTarget.  # noqa: E501


        :return: The target_path of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """Sets the target_path of this DetectionsForTarget.


        :param target_path: The target_path of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_path = target_path

    @property
    def target_port(self):
        """Gets the target_port of this DetectionsForTarget.  # noqa: E501


        :return: The target_port of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """Sets the target_port of this DetectionsForTarget.


        :param target_port: The target_port of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._target_port = target_port

    @property
    def target_protocol(self):
        """Gets the target_protocol of this DetectionsForTarget.  # noqa: E501


        :return: The target_protocol of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._target_protocol

    @target_protocol.setter
    def target_protocol(self, target_protocol):
        """Sets the target_protocol of this DetectionsForTarget.


        :param target_protocol: The target_protocol of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._target_protocol = target_protocol

    @property
    def target_temptation(self):
        """Gets the target_temptation of this DetectionsForTarget.  # noqa: E501


        :return: The target_temptation of this DetectionsForTarget.  # noqa: E501
        :rtype: int
        """
        return self._target_temptation

    @target_temptation.setter
    def target_temptation(self, target_temptation):
        """Sets the target_temptation of this DetectionsForTarget.


        :param target_temptation: The target_temptation of this DetectionsForTarget.  # noqa: E501
        :type: int
        """

        self._target_temptation = target_temptation

    @property
    def thumbnail_uuid(self):
        """Gets the thumbnail_uuid of this DetectionsForTarget.  # noqa: E501


        :return: The thumbnail_uuid of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_uuid

    @thumbnail_uuid.setter
    def thumbnail_uuid(self, thumbnail_uuid):
        """Sets the thumbnail_uuid of this DetectionsForTarget.


        :param thumbnail_uuid: The thumbnail_uuid of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._thumbnail_uuid = thumbnail_uuid

    @property
    def vendor(self):
        """Gets the vendor of this DetectionsForTarget.  # noqa: E501


        :return: The vendor of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DetectionsForTarget.


        :param vendor: The vendor of this DetectionsForTarget.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this DetectionsForTarget.  # noqa: E501


        :return: The version of this DetectionsForTarget.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DetectionsForTarget.


        :param version: The version of this DetectionsForTarget.  # noqa: E501
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
        if not isinstance(other, DetectionsForTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetectionsForTarget):
            return True

        return self.to_dict() != other.to_dict()
