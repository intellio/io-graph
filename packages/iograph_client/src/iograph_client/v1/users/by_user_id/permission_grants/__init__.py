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
	from .by_resource_specific_permission_grant_id import ByResourceSpecificPermissionGrantIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.resource_specific_permission_grant_collection_response import ResourceSpecificPermissionGrantCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.resource_specific_permission_grant import ResourceSpecificPermissionGrant


class PermissionGrantsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/permissionGrants", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ResourceSpecificPermissionGrantCollectionResponse:
		"""
		List permissionGrants of a user
		List all resource-specific permission grants of a user. This list specifies the Microsoft Entra apps that have access to the user, along with the corresponding resource-specific access that each app has.
		Find more info here: https://learn.microsoft.com/graph/api/user-list-permissiongrants?view=graph-rest-1.0
		"""
		tags = ['users.resourceSpecificPermissionGrant']

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
		return await self.request_adapter.send_async(request_info, ResourceSpecificPermissionGrantCollectionResponse, error_mapping)

	async def post(
		self,
		body: ResourceSpecificPermissionGrant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ResourceSpecificPermissionGrant:
		"""
		Create new navigation property to permissionGrants for users
		
		"""
		tags = ['users.resourceSpecificPermissionGrant']

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
		return await self.request_adapter.send_async(request_info, ResourceSpecificPermissionGrant, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PermissionGrantsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PermissionGrantsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	def by_resource_specific_permission_grant_id(self,
		user_id: str,
		resourceSpecificPermissionGrant_id: str,
	) -> ByResourceSpecificPermissionGrantIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if resourceSpecificPermissionGrant_id is None:
			raise TypeError("resourceSpecificPermissionGrant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["resourceSpecificPermissionGrant%2Did"] =  resourceSpecificPermissionGrant_id

		from .by_resource_specific_permission_grant_id import ByResourceSpecificPermissionGrantIdRequest
		return ByResourceSpecificPermissionGrantIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

