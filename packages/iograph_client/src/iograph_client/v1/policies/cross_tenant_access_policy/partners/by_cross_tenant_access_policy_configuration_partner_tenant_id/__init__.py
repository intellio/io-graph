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
	from .identity_synchronization import IdentitySynchronizationRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/crossTenantAccessPolicy/partners/{crossTenantAccessPolicyConfigurationPartner%2DtenantId}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CrossTenantAccessPolicyConfigurationPartner:
		"""
		Get crossTenantAccessPolicyConfigurationPartner
		Read the properties and relationships of a partner-specific configuration.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicyconfigurationpartner-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicyConfigurationPartner, error_mapping)

	async def patch(
		self,
		body: CrossTenantAccessPolicyConfigurationPartner,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CrossTenantAccessPolicyConfigurationPartner:
		"""
		Update crossTenantAccessPolicyConfigurationPartner
		Update the properties of a partner-specific configuration.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicyconfigurationpartner-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicyConfigurationPartner, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete crossTenantAccessPolicyConfigurationPartner
		Delete a partner-specific configuration in a cross-tenant access policy. If a configuration includes a user synchronization policy, you must first delete the user synchronization policy before you can delete the partner-specific configuration.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicyconfigurationpartner-delete?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest(self.request_adapter, self.path_parameters)

	def identity_synchronization(self,
		crossTenantAccessPolicyConfigurationPartner_tenantId: str,
	) -> IdentitySynchronizationRequest:
		if crossTenantAccessPolicyConfigurationPartner_tenantId is None:
			raise TypeError("crossTenantAccessPolicyConfigurationPartner_tenantId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["crossTenantAccessPolicyConfigurationPartner%2DtenantId"] =  crossTenantAccessPolicyConfigurationPartner_tenantId

		from .identity_synchronization import IdentitySynchronizationRequest
		return IdentitySynchronizationRequest(self.request_adapter, path_parameters)

