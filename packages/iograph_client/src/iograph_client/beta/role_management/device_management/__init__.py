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
	from .role_definitions import RoleDefinitionsRequest
	from .role_assignments import RoleAssignmentsRequest
	from .resource_namespaces import ResourceNamespacesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.rbac_application_multiple import RbacApplicationMultiple
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/deviceManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RbacApplicationMultiple:
		"""
		Get deviceManagement from roleManagement
		The RbacApplication for Device Management
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
		return await self.request_adapter.send_async(request_info, RbacApplicationMultiple, error_mapping)

	async def patch(
		self,
		body: RbacApplicationMultiple,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RbacApplicationMultiple:
		"""
		Update the navigation property deviceManagement in roleManagement
		
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
		return await self.request_adapter.send_async(request_info, RbacApplicationMultiple, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property deviceManagement for roleManagement
		
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



	def with_url(self, raw_url: str) -> DeviceManagementRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceManagementRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_namespaces(self,
	) -> ResourceNamespacesRequest:
		from .resource_namespaces import ResourceNamespacesRequest
		return ResourceNamespacesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_assignments(self,
	) -> RoleAssignmentsRequest:
		from .role_assignments import RoleAssignmentsRequest
		return RoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_definitions(self,
	) -> RoleDefinitionsRequest:
		from .role_definitions import RoleDefinitionsRequest
		return RoleDefinitionsRequest(self.request_adapter, self.path_parameters)

