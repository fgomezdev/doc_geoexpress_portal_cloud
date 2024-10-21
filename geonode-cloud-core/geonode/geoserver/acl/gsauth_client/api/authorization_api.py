# coding: utf-8

"""
    GeoServer ACL

    GeoServer Access Control List API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from geonode.geoserver.acl.gsauth_client.api_client import ApiClient
from geonode.geoserver.acl.gsauth_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuthorizationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_access_info(self, access_request, **kwargs):  # noqa: E501
        """get_access_info  # noqa: E501

        Computes the grant access info for the given request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_info(access_request, async_req=True)
        >>> result = thread.get()

        :param access_request: (required)
        :type access_request: AccessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccessInfo
        """
        kwargs['_return_http_data_only'] = True
        return self.get_access_info_with_http_info(access_request, **kwargs)  # noqa: E501

    def get_access_info_with_http_info(self, access_request, **kwargs):  # noqa: E501
        """get_access_info  # noqa: E501

        Computes the grant access info for the given request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_info_with_http_info(access_request, async_req=True)
        >>> result = thread.get()

        :param access_request: (required)
        :type access_request: AccessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccessInfo, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'access_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'access_request' is set
        if self.api_client.client_side_validation and local_var_params.get('access_request') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `access_request` when calling `get_access_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'access_request' in local_var_params:
            body_params = local_var_params['access_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/x-jackson-smile'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/x-jackson-smile'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        response_types_map = {
            200: "AccessInfo",
        }

        return self.api_client.call_api(
            '/authorization/resources', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_admin_authorization(self, admin_access_request, **kwargs):  # noqa: E501
        """get_admin_authorization  # noqa: E501

        Computes info about admin authorization on a given workspace. Returned AccessInfo will always be ALLOW, with the computed adminRights.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_admin_authorization(admin_access_request, async_req=True)
        >>> result = thread.get()

        :param admin_access_request: (required)
        :type admin_access_request: AdminAccessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AdminAccessInfo
        """
        kwargs['_return_http_data_only'] = True
        return self.get_admin_authorization_with_http_info(admin_access_request, **kwargs)  # noqa: E501

    def get_admin_authorization_with_http_info(self, admin_access_request, **kwargs):  # noqa: E501
        """get_admin_authorization  # noqa: E501

        Computes info about admin authorization on a given workspace. Returned AccessInfo will always be ALLOW, with the computed adminRights.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_admin_authorization_with_http_info(admin_access_request, async_req=True)
        >>> result = thread.get()

        :param admin_access_request: (required)
        :type admin_access_request: AdminAccessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AdminAccessInfo, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'admin_access_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_authorization" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'admin_access_request' is set
        if self.api_client.client_side_validation and local_var_params.get('admin_access_request') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `admin_access_request` when calling `get_admin_authorization`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'admin_access_request' in local_var_params:
            body_params = local_var_params['admin_access_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/x-jackson-smile'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/x-jackson-smile'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        response_types_map = {
            200: "AdminAccessInfo",
        }

        return self.api_client.call_api(
            '/authorization/admin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_matching_rules(self, access_request, **kwargs):  # noqa: E501
        """get_matching_rules  # noqa: E501

        Obtains the plain list of matching rules that are applied to the given AccessRequest when computing the AccessInfo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_matching_rules(access_request, async_req=True)
        >>> result = thread.get()

        :param access_request: (required)
        :type access_request: AccessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[Rule]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_matching_rules_with_http_info(access_request, **kwargs)  # noqa: E501

    def get_matching_rules_with_http_info(self, access_request, **kwargs):  # noqa: E501
        """get_matching_rules  # noqa: E501

        Obtains the plain list of matching rules that are applied to the given AccessRequest when computing the AccessInfo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_matching_rules_with_http_info(access_request, async_req=True)
        >>> result = thread.get()

        :param access_request: (required)
        :type access_request: AccessRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[Rule], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'access_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_matching_rules" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'access_request' is set
        if self.api_client.client_side_validation and local_var_params.get('access_request') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `access_request` when calling `get_matching_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'access_request' in local_var_params:
            body_params = local_var_params['access_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/x-jackson-smile'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/x-jackson-smile'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        response_types_map = {
            200: "list[Rule]",
        }

        return self.api_client.call_api(
            '/authorization/resources/matchingrules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
