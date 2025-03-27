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
	from .by_unified_rbac_resource_action_id import ByUnifiedRbacResourceActionIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.unified_rbac_resource_action import UnifiedRbacResourceAction
from iograph_models.v1.unified_rbac_resource_action_collection_response import UnifiedRbacResourceActionCollectionResponse


class ResourceActionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/directory/resourceNamespaces/{unifiedRbacResourceNamespace%2Did}/resourceActions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRbacResourceActionCollectionResponse:
		"""
		Get resourceActions from roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRbacResourceActionCollectionResponse, error_mapping)

	async def post(
		self,
		body: UnifiedRbacResourceAction,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRbacResourceAction:
		"""
		Create new navigation property to resourceActions for roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRbacResourceAction, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ResourceActionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ResourceActionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ResourceActionsRequest(self.request_adapter, self.path_parameters)

	def by_unified_rbac_resource_action_id(self,
		unifiedRbacResourceNamespace_id: str,
		unifiedRbacResourceAction_id: str,
	) -> ByUnifiedRbacResourceActionIdRequest:
		if unifiedRbacResourceNamespace_id is None:
			raise TypeError("unifiedRbacResourceNamespace_id cannot be null.")
		if unifiedRbacResourceAction_id is None:
			raise TypeError("unifiedRbacResourceAction_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRbacResourceNamespace%2Did"] =  unifiedRbacResourceNamespace_id
		path_parameters["unifiedRbacResourceAction%2Did"] =  unifiedRbacResourceAction_id

		from .by_unified_rbac_resource_action_id import ByUnifiedRbacResourceActionIdRequest
		return ByUnifiedRbacResourceActionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		unifiedRbacResourceNamespace_id: str,
	) -> CountRequest:
		if unifiedRbacResourceNamespace_id is None:
			raise TypeError("unifiedRbacResourceNamespace_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRbacResourceNamespace%2Did"] =  unifiedRbacResourceNamespace_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

