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


class TextFilter(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name and the value is attribute type.
      attribute_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_types = {
        'include_default': 'bool',
        'value': 'str'
    }

    attribute_map = {
        'include_default': 'includeDefault',
        'value': 'value'
    }

    def __init__(self, include_default=None, value=None, local_vars_configuration=None):  # noqa: E501
        """TextFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._include_default = None
        self._value = None
        self.discriminator = None

        self.include_default = include_default
        self.value = value

    @property
    def include_default(self):
        """Gets the include_default of this TextFilter.  # noqa: E501


        :return: The include_default of this TextFilter.  # noqa: E501
        :rtype: bool
        """
        return self._include_default

    @include_default.setter
    def include_default(self, include_default):
        """Sets the include_default of this TextFilter.


        :param include_default: The include_default of this TextFilter.  # noqa: E501
        :type include_default: bool
        """

        self._include_default = include_default

    @property
    def value(self):
        """Gets the value of this TextFilter.  # noqa: E501

        An absent value will match both set and default values for the property, a value with only the character literal '*' will match only the default values for the property, any other specific value will match properties with that value  # noqa: E501

        :return: The value of this TextFilter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TextFilter.

        An absent value will match both set and default values for the property, a value with only the character literal '*' will match only the default values for the property, any other specific value will match properties with that value  # noqa: E501

        :param value: The value of this TextFilter.  # noqa: E501
        :type value: str
        """

        self._value = value

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
        if not isinstance(other, TextFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextFilter):
            return True

        return self.to_dict() != other.to_dict()
