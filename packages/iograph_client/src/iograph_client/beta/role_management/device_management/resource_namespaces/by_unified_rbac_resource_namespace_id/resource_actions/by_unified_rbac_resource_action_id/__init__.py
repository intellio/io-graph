# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .resource_scope import ResourceScopeRequest
	from .authentication_context import AuthenticationContextRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.unified_rbac_resource_action import UnifiedRbacResourceAction


class ByUnifiedRbacResourceActionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/deviceManagement/resourceNamespaces/{unifiedRbacResourceNamespace%2Did}/resourceActions/{unifiedRbacResourceAction%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRbacResourceAction:
		"""
		Get resourceActions from roleManagement
		Operations that an authorized principal is allowed to perform.
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
		return await self.request_adapter.send_async(request_info, UnifiedRbacResourceAction, error_mapping)

	async def patch(
		self,
		body: UnifiedRbacResourceAction,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRbacResourceAction:
		"""
		Update the navigation property resourceActions in roleManagement
		
		"""
		tags = ['roleManagement.rbacApplicationMultiple']

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
		return await self.request_adapter.send_async(request_info, UnifiedRbacResourceAction, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property resourceActions for roleManagement
		
		"""
		tags = ['roleManagement.rbacApplicationMultiple']
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



	def with_url(self, raw_url: str) -> ByUnifiedRbacResourceActionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedRbacResourceActionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedRbacResourceActionIdRequest(self.request_adapter, self.path_parameters)

	def authentication_context(self,
		unifiedRbacResourceNamespace_id: str,
		unifiedRbacResourceAction_id: str,
	) -> AuthenticationContextRequest:
		if unifiedRbacResourceNamespace_id is None:
			raise TypeError("unifiedRbacResourceNamespace_id cannot be null.")
		if unifiedRbacResourceAction_id is None:
			raise TypeError("unifiedRbacResourceAction_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRbacResourceNamespace%2Did"] =  unifiedRbacResourceNamespace_id
		path_parameters["unifiedRbacResourceAction%2Did"] =  unifiedRbacResourceAction_id

		from .authentication_context import AuthenticationContextRequest
		return AuthenticationContextRequest(self.request_adapter, path_parameters)

	def resource_scope(self,
		unifiedRbacResourceNamespace_id: str,
		unifiedRbacResourceAction_id: str,
	) -> ResourceScopeRequest:
		if unifiedRbacResourceNamespace_id is None:
			raise TypeError("unifiedRbacResourceNamespace_id cannot be null.")
		if unifiedRbacResourceAction_id is None:
			raise TypeError("unifiedRbacResourceAction_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRbacResourceNamespace%2Did"] =  unifiedRbacResourceNamespace_id
		path_parameters["unifiedRbacResourceAction%2Did"] =  unifiedRbacResourceAction_id

		from .resource_scope import ResourceScopeRequest
		return ResourceScopeRequest(self.request_adapter, path_parameters)

