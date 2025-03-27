# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .versions import VersionsRequest
	from .management_template import ManagementTemplateRequest
	from .accepted_version import AcceptedVersionRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_tenants_management_template_step import ManagedTenantsManagementTemplateStep
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByManagementTemplateStepIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managementTemplateSteps/{managementTemplateStep%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedTenantsManagementTemplateStep:
		"""
		Get managementTemplateSteps from tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagementTemplateStep, error_mapping)

	async def patch(
		self,
		body: ManagedTenantsManagementTemplateStep,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedTenantsManagementTemplateStep:
		"""
		Update the navigation property managementTemplateSteps in tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, ManagedTenantsManagementTemplateStep, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property managementTemplateSteps for tenantRelationships
		
		"""
		tags = ['tenantRelationships.managedTenant']
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



	def with_url(self, raw_url: str) -> ByManagementTemplateStepIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByManagementTemplateStepIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByManagementTemplateStepIdRequest(self.request_adapter, self.path_parameters)

	def accepted_version(self,
		managementTemplateStep_id: str,
	) -> AcceptedVersionRequest:
		if managementTemplateStep_id is None:
			raise TypeError("managementTemplateStep_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managementTemplateStep%2Did"] =  managementTemplateStep_id

		from .accepted_version import AcceptedVersionRequest
		return AcceptedVersionRequest(self.request_adapter, path_parameters)

	def management_template(self,
		managementTemplateStep_id: str,
	) -> ManagementTemplateRequest:
		if managementTemplateStep_id is None:
			raise TypeError("managementTemplateStep_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managementTemplateStep%2Did"] =  managementTemplateStep_id

		from .management_template import ManagementTemplateRequest
		return ManagementTemplateRequest(self.request_adapter, path_parameters)

	def versions(self,
		managementTemplateStep_id: str,
	) -> VersionsRequest:
		if managementTemplateStep_id is None:
			raise TypeError("managementTemplateStep_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managementTemplateStep%2Did"] =  managementTemplateStep_id

		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, path_parameters)

