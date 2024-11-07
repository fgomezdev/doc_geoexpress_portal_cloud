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


class AdminAccessInfo(object):
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
        'admin': 'bool',
        'workspace': 'str',
        'matching_admin_rule': 'str'
    }

    attribute_map = {
        'admin': 'admin',
        'workspace': 'workspace',
        'matching_admin_rule': 'matchingAdminRule'
    }

    def __init__(self, admin=None, workspace=None, matching_admin_rule=None, local_vars_configuration=None):  # noqa: E501
        """AdminAccessInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._admin = None
        self._workspace = None
        self._matching_admin_rule = None
        self.discriminator = None

        self.admin = admin
        if workspace is not None:
            self.workspace = workspace
        if matching_admin_rule is not None:
            self.matching_admin_rule = matching_admin_rule

    @property
    def admin(self):
        """Gets the admin of this AdminAccessInfo.  # noqa: E501


        :return: The admin of this AdminAccessInfo.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this AdminAccessInfo.


        :param admin: The admin of this AdminAccessInfo.  # noqa: E501
        :type admin: bool
        """
        if self.local_vars_configuration.client_side_validation and admin is None:  # noqa: E501
            raise ValueError("Invalid value for `admin`, must not be `None`")  # noqa: E501

        self._admin = admin

    @property
    def workspace(self):
        """Gets the workspace of this AdminAccessInfo.  # noqa: E501


        :return: The workspace of this AdminAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this AdminAccessInfo.


        :param workspace: The workspace of this AdminAccessInfo.  # noqa: E501
        :type workspace: str
        """

        self._workspace = workspace

    @property
    def matching_admin_rule(self):
        """Gets the matching_admin_rule of this AdminAccessInfo.  # noqa: E501


        :return: The matching_admin_rule of this AdminAccessInfo.  # noqa: E501
        :rtype: str
        """
        return self._matching_admin_rule

    @matching_admin_rule.setter
    def matching_admin_rule(self, matching_admin_rule):
        """Sets the matching_admin_rule of this AdminAccessInfo.


        :param matching_admin_rule: The matching_admin_rule of this AdminAccessInfo.  # noqa: E501
        :type matching_admin_rule: str
        """

        self._matching_admin_rule = matching_admin_rule

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
        if not isinstance(other, AdminAccessInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdminAccessInfo):
            return True

        return self.to_dict() != other.to_dict()
