# coding: utf-8

"""
    GeoServer ACL

    GeoServer Access Control List API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from geonode.geoserver.acl.gsauth_client.configuration import Configuration


class AccessInfo(object):
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
        'grant': 'GrantType',
        'area': 'Geom',
        'clip_area': 'Geom',
        'catalog_mode': 'CatalogMode',
        'default_style': 'str',
        'allowed_styles': 'list[str]',
        'cql_filter_read': 'str',
        'cql_filter_write': 'str',
        'attributes': 'list[LayerAttribute]',
        'matching_rules': 'list[str]'
    }

    attribute_map = {
        'grant': 'grant',
        'area': 'area',
        'clip_area': 'clipArea',
        'catalog_mode': 'catalogMode',
        'default_style': 'defaultStyle',
        'allowed_styles': 'allowedStyles',
        'cql_filter_read': 'cqlFilterRead',
        'cql_filter_write': 'cqlFilterWrite',
        'attributes': 'attributes',
        'matching_rules': 'matchingRules'
    }

    def __init__(self, grant=None, area=None, clip_area=None, catalog_mode=None, default_style=None, allowed_styles=None, cql_filter_read=None, cql_filter_write=None, attributes=None, matching_rules=None, local_vars_configuration=None):  # noqa: E501
        """AccessInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._grant = None
        self._area = None
        self._clip_area = None
        self._catalog_mode = None
        self._default_style = None
        self._allowed_styles = None
        self._cql_filter_read = None
        self._cql_filter_write = None
        self._attributes = None
        self._matching_rules = None
        self.discriminator = None

        self.grant = grant
        if area is not None:
            self.area = area
        if clip_area is not None:
            self.clip_area = clip_area
        self.catalog_mode = catalog_mode
        if default_style is not None:
            self.default_style = default_style
        if allowed_styles is not None:
            self.allowed_styles = allowed_styles
        if cql_filter_read is not None:
            self.cql_filter_read = cql_filter_read
        if cql_filter_write is not None:
            self.cql_filter_write = cql_filter_write
        self.attributes = attributes
        if matching_rules is not None:
            self.matching_rules = matching_rules

    @property
    def grant(self):
        """Gets the grant of this AccessInfo.  # noqa: E501


        :return: The grant of this AccessInfo.  # noqa: E501
        :rtype: GrantType
        """
        return self._grant

    @grant.setter
    def grant(self, grant):
        """Sets the grant of this AccessInfo.


        :param grant: The grant of this AccessInfo.  # noqa: E501
        :type grant: GrantType
        """

        self._grant = grant

    @property
    def area(self):
        """Gets the area of this AccessInfo.  # noqa: E501


        :return: The area of this AccessInfo.  # noqa: E501
        :rtype: Geom
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this AccessInfo.


        :param area: The area of this AccessInfo.  # noqa: E501
        :type area: Geom
        """

        self._area = area

    @property
    def clip_area(self):
        """Gets the clip_area of this AccessInfo.  # noqa: E501


        :return: The clip_area of this AccessInfo.  # noqa: E501
        :rtype: Geom
        """
        return self._clip_area

    @clip_area.setter
    def clip_area(self, clip_area):
        """Sets the clip_area of this AccessInfo.


        :param clip_area: The clip_area of this AccessInfo.  # noqa: E501
        :type clip_area: Geom
        """

        self._clip_area = clip_area

    @property
    def catalog_mode(self):
        """Gets the catalog_mode of this AccessInfo.  # noqa: E501


        :return: The catalog_mode of this AccessInfo.  # noqa: E501
        :rtype: CatalogMode
        """
        return self._catalog_mode

    @catalog_mode.setter
    def catalog_mode(self, catalog_mode):
        """Sets the catalog_mode of this AccessInfo.


        :param catalog_mode: The catalog_mode of this AccessInfo.  # noqa: E501
        :type catalog_mode: CatalogMode
        """

        self._catalog_mode = catalog_mode

    @property
    def default_style(self):
        """Gets the default_style of this AccessInfo.  # noqa: E501


        :return: The default_style of this AccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_style

    @default_style.setter
    def default_style(self, default_style):
        """Sets the default_style of this AccessInfo.


        :param default_style: The default_style of this AccessInfo.  # noqa: E501
        :type default_style: str
        """

        self._default_style = default_style

    @property
    def allowed_styles(self):
        """Gets the allowed_styles of this AccessInfo.  # noqa: E501


        :return: The allowed_styles of this AccessInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_styles

    @allowed_styles.setter
    def allowed_styles(self, allowed_styles):
        """Sets the allowed_styles of this AccessInfo.


        :param allowed_styles: The allowed_styles of this AccessInfo.  # noqa: E501
        :type allowed_styles: list[str]
        """

        self._allowed_styles = allowed_styles

    @property
    def cql_filter_read(self):
        """Gets the cql_filter_read of this AccessInfo.  # noqa: E501


        :return: The cql_filter_read of this AccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._cql_filter_read

    @cql_filter_read.setter
    def cql_filter_read(self, cql_filter_read):
        """Sets the cql_filter_read of this AccessInfo.


        :param cql_filter_read: The cql_filter_read of this AccessInfo.  # noqa: E501
        :type cql_filter_read: str
        """

        self._cql_filter_read = cql_filter_read

    @property
    def cql_filter_write(self):
        """Gets the cql_filter_write of this AccessInfo.  # noqa: E501


        :return: The cql_filter_write of this AccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._cql_filter_write

    @cql_filter_write.setter
    def cql_filter_write(self, cql_filter_write):
        """Sets the cql_filter_write of this AccessInfo.


        :param cql_filter_write: The cql_filter_write of this AccessInfo.  # noqa: E501
        :type cql_filter_write: str
        """

        self._cql_filter_write = cql_filter_write

    @property
    def attributes(self):
        """Gets the attributes of this AccessInfo.  # noqa: E501


        :return: The attributes of this AccessInfo.  # noqa: E501
        :rtype: list[LayerAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AccessInfo.


        :param attributes: The attributes of this AccessInfo.  # noqa: E501
        :type attributes: list[LayerAttribute]
        """

        self._attributes = attributes

    @property
    def matching_rules(self):
        """Gets the matching_rules of this AccessInfo.  # noqa: E501


        :return: The matching_rules of this AccessInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._matching_rules

    @matching_rules.setter
    def matching_rules(self, matching_rules):
        """Sets the matching_rules of this AccessInfo.


        :param matching_rules: The matching_rules of this AccessInfo.  # noqa: E501
        :type matching_rules: list[str]
        """

        self._matching_rules = matching_rules

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccessInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessInfo):
            return True

        return self.to_dict() != other.to_dict()