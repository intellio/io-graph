# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_app_scope_id import ByAppScopeIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.app_scope_collection_response import AppScopeCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.app_scope import AppScope


class AppScopesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/deviceManagement/roleAssignments/{unifiedRoleAssignmentMultiple%2Did}/appScopes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AppScopeCollectionResponse:
		"""
		Get appScopes from roleManagement
		Read-only collection with details of the app specific scopes when the assignment scopes are app specific. Containment entity. Read-only.
		"""
		tags = ['roleManagement.rbacApplicationMultiple']

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
		return await self.request_adapter.send_async(request_info, AppScopeCollectionResponse, error_mapping)

	async def post(
		self,
		body: AppScope,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AppScope:
		"""
		Create new navigation property to appScopes for roleManagement
		
		"""
		tags = ['roleManagement.rbacApplicationMultiple']

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
		return await self.request_adapter.send_async(request_info, AppScope, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AppScopesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AppScopesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AppScopesRequest(self.request_adapter, self.path_parameters)

	def by_app_scope_id(self,
		unifiedRoleAssignmentMultiple_id: str,
		appScope_id: str,
	) -> ByAppScopeIdRequest:
		if unifiedRoleAssignmentMultiple_id is None:
			raise TypeError("unifiedRoleAssignmentMultiple_id cannot be null.")
		if appScope_id is None:
			raise TypeError("appScope_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleAssignmentMultiple%2Did"] =  unifiedRoleAssignmentMultiple_id
		path_parameters["appScope%2Did"] =  appScope_id

		from .by_app_scope_id import ByAppScopeIdRequest
		return ByAppScopeIdRequest(self.request_adapter, path_parameters)

	def count(self,
		unifiedRoleAssignmentMultiple_id: str,
	) -> CountRequest:
		if unifiedRoleAssignmentMultiple_id is None:
			raise TypeError("unifiedRoleAssignmentMultiple_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleAssignmentMultiple%2Did"] =  unifiedRoleAssignmentMultiple_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

