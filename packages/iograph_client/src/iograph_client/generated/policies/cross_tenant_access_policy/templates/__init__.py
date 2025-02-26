# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .multi_tenant_organization_partner_configuration import MultiTenantOrganizationPartnerConfigurationRequest
	from .multi_tenant_organization_identity_synchronization import MultiTenantOrganizationIdentitySynchronizationRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.policy_template import PolicyTemplate


class TemplatesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/policies/crossTenantAccessPolicy/templates"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PolicyTemplate:
		"""
		Get templates from policies
		Represents the base policy in the directory for multitenant organization settings.
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, PolicyTemplate, error_mapping)

	async def patch(
		self,
		body: PolicyTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PolicyTemplate:
		"""
		Update the navigation property templates in policies
		
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, PolicyTemplate, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property templates for policies
		
		"""
		tags = ['policies.crossTenantAccessPolicy']
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



	@property
	def multi_tenant_organization_identity_synchronization(self,
	) -> MultiTenantOrganizationIdentitySynchronizationRequest:
		from .multi_tenant_organization_identity_synchronization import MultiTenantOrganizationIdentitySynchronizationRequest
		return MultiTenantOrganizationIdentitySynchronizationRequest(self.request_adapter, self.path_parameters)

	@property
	def multi_tenant_organization_partner_configuration(self,
	) -> MultiTenantOrganizationPartnerConfigurationRequest:
		from .multi_tenant_organization_partner_configuration import MultiTenantOrganizationPartnerConfigurationRequest
		return MultiTenantOrganizationPartnerConfigurationRequest(self.request_adapter, self.path_parameters)

