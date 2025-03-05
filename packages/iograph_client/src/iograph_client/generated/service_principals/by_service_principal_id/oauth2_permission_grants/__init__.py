# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_o_auth2_permission_grant_id import ByOAuth2PermissionGrantIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.o_auth2_permission_grant_collection_response import OAuth2PermissionGrantCollectionResponse


class Oauth2PermissionGrantsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/oauth2PermissionGrants", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OAuth2PermissionGrantCollectionResponse:
		"""
		List oauth2PermissionGrants granted to a service principal
		Retrieve a list of oAuth2PermissionGrant entities, representing delegated permissions granted to the service principal (representing the client application) to access an API on behalf of a user.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list-oauth2permissiongrants?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.oAuth2PermissionGrant']

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
		return await self.request_adapter.send_async(request_info, OAuth2PermissionGrantCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> Oauth2PermissionGrantsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: Oauth2PermissionGrantsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return Oauth2PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	def by_o_auth2_permission_grant_id(self,
		servicePrincipal_id: str,
		oAuth2PermissionGrant_id: str,
	) -> ByOAuth2PermissionGrantIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if oAuth2PermissionGrant_id is None:
			raise TypeError("oAuth2PermissionGrant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["oAuth2PermissionGrant%2Did"] =  oAuth2PermissionGrant_id

		from .by_o_auth2_permission_grant_id import ByOAuth2PermissionGrantIdRequest
		return ByOAuth2PermissionGrantIdRequest(self.request_adapter, path_parameters)

	def count(self,
		servicePrincipal_id: str,
	) -> CountRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

