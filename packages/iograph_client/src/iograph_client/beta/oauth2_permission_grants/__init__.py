# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_o_auth2_permission_grant_id import ByOAuth2PermissionGrantIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_auth2_permission_grant_collection_response import OAuth2PermissionGrantCollectionResponse
from iograph_models.beta.o_auth2_permission_grant import OAuth2PermissionGrant
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class Oauth2PermissionGrantsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/oauth2PermissionGrants", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OAuth2PermissionGrantCollectionResponse:
		"""
		List oauth2PermissionGrants (delegated permission grants)
		Retrieve a list of oAuth2PermissionGrant objects, representing delegated permissions which have been granted for client applications to access APIs on behalf of signed-in users.
		Find more info here: https://learn.microsoft.com/graph/api/oauth2permissiongrant-list?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, OAuth2PermissionGrantCollectionResponse, error_mapping)

	async def post(
		self,
		body: OAuth2PermissionGrant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OAuth2PermissionGrant:
		"""
		Create oAuth2PermissionGrant (a delegated permission grant)
		Create a delegated permission grant, represented by an oAuth2PermissionGrant object. A delegated permission grant authorizes a client service principal (representing a client application) to access a resource service principal (representing an API), on behalf of a signed-in user, for the level of access limited by the delegated permissions which were granted.
		Find more info here: https://learn.microsoft.com/graph/api/oauth2permissiongrant-post?view=graph-rest-beta
		"""
		tags = ['oauth2PermissionGrants.oAuth2PermissionGrant']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, OAuth2PermissionGrant, error_mapping)

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
		oAuth2PermissionGrant_id: str,
	) -> ByOAuth2PermissionGrantIdRequest:
		if oAuth2PermissionGrant_id is None:
			raise TypeError("oAuth2PermissionGrant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["oAuth2PermissionGrant%2Did"] =  oAuth2PermissionGrant_id

		from .by_o_auth2_permission_grant_id import ByOAuth2PermissionGrantIdRequest
		return ByOAuth2PermissionGrantIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

