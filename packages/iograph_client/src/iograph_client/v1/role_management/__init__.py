# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .entitlement_management import EntitlementManagementRequest
	from .directory import DirectoryRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.role_management import RoleManagement


class RoleManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RoleManagement:
		"""
		Get roleManagement
		
		"""
		tags = ['roleManagement.roleManagement']

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
		return await self.request_adapter.send_async(request_info, RoleManagement, error_mapping)

	async def patch(
		self,
		body: RoleManagement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RoleManagement:
		"""
		Update roleManagement
		
		"""
		tags = ['roleManagement.roleManagement']

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
		return await self.request_adapter.send_async(request_info, RoleManagement, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RoleManagementRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RoleManagementRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RoleManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def directory(self,
	) -> DirectoryRequest:
		from .directory import DirectoryRequest
		return DirectoryRequest(self.request_adapter, self.path_parameters)

	@property
	def entitlement_management(self,
	) -> EntitlementManagementRequest:
		from .entitlement_management import EntitlementManagementRequest
		return EntitlementManagementRequest(self.request_adapter, self.path_parameters)

