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
	from .by_cross_tenant_access_policy_configuration_partner_tenant_id import ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.cross_tenant_access_policy_configuration_partner_collection_response import CrossTenantAccessPolicyConfigurationPartnerCollectionResponse


class PartnersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/crossTenantAccessPolicy/partners", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CrossTenantAccessPolicyConfigurationPartnerCollectionResponse:
		"""
		List partners
		Get a list of all partner configurations within a cross-tenant access policy. You can also use the $expand parameter to list the user synchronization policy for all partner configurations.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicy-list-partners?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicyConfigurationPartnerCollectionResponse, error_mapping)

	async def post(
		self,
		body: CrossTenantAccessPolicyConfigurationPartner,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CrossTenantAccessPolicyConfigurationPartner:
		"""
		Create crossTenantAccessPolicyConfigurationPartner
		Create a new partner configuration in a cross-tenant access policy.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicy-post-partners?view=graph-rest-beta
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicyConfigurationPartner, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PartnersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PartnersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PartnersRequest(self.request_adapter, self.path_parameters)

	def by_cross_tenant_access_policy_configuration_partner_tenant_id(self,
		crossTenantAccessPolicyConfigurationPartner_tenantId: str,
	) -> ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest:
		if crossTenantAccessPolicyConfigurationPartner_tenantId is None:
			raise TypeError("crossTenantAccessPolicyConfigurationPartner_tenantId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["crossTenantAccessPolicyConfigurationPartner%2DtenantId"] =  crossTenantAccessPolicyConfigurationPartner_tenantId

		from .by_cross_tenant_access_policy_configuration_partner_tenant_id import ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest
		return ByCrossTenantAccessPolicyConfigurationPartnerTenantIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

