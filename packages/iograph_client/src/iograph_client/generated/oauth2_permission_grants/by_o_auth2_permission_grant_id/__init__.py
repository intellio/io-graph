# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.o_auth2_permission_grant import OAuth2PermissionGrant


class ByOAuth2PermissionGrantIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/oauth2PermissionGrants/{oAuth2PermissionGrant%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OAuth2PermissionGrant:
		"""
		Get oAuth2PermissionGrant (a delegated permission grant)
		Retrieve the properties of a single delegated permission grant represented by an oAuth2PermissionGrant object. An oAuth2PermissionGrant represents delegated permissions which have been granted for a client application to access an API on behalf of a signed-in user.
		Find more info here: https://learn.microsoft.com/graph/api/oauth2permissiongrant-get?view=graph-rest-1.0
		"""
		tags = ['oauth2PermissionGrants.oAuth2PermissionGrant']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, OAuth2PermissionGrant, error_mapping)

	async def patch(
		self,
		body: OAuth2PermissionGrant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OAuth2PermissionGrant:
		"""
		Update a delegated permission grant (oAuth2PermissionGrant)
		Update the properties of oAuth2PermissionGrant object, representing a delegated permission grant. An oAuth2PermissionGrant can be updated to change which delegated permissions are granted, by adding or removing items from the list in scopes.
		Find more info here: https://learn.microsoft.com/graph/api/oauth2permissiongrant-update?view=graph-rest-1.0
		"""
		tags = ['oauth2PermissionGrants.oAuth2PermissionGrant']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, OAuth2PermissionGrant, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete oAuth2PermissionGrant (a delegated permission grant)
		Delete a delegated permission grant, represented by an oAuth2PermissionGrant object. When a delegated permission grant is deleted, the access it granted is revoked. Existing access tokens will continue to be valid for their lifetime, but new access tokens will not be granted for the delegated permissions identified in the deleted oAuth2PermissionGrant.
		Find more info here: https://learn.microsoft.com/graph/api/oauth2permissiongrant-delete?view=graph-rest-1.0
		"""
		tags = ['oauth2PermissionGrants.oAuth2PermissionGrant']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByOAuth2PermissionGrantIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOAuth2PermissionGrantIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOAuth2PermissionGrantIdRequest(self.request_adapter, self.path_parameters)

