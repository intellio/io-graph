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
	from .tenants import TenantsRequest
	from .join_request import JoinRequestRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.multi_tenant_organization import MultiTenantOrganization


class MultiTenantOrganizationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/multiTenantOrganization", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MultiTenantOrganization:
		"""
		Get multiTenantOrganization
		Get properties of the multitenant organization.
		Find more info here: https://learn.microsoft.com/graph/api/multitenantorganization-get?view=graph-rest-beta
		"""
		tags = ['tenantRelationships.multiTenantOrganization']

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
		return await self.request_adapter.send_async(request_info, MultiTenantOrganization, error_mapping)

	async def patch(
		self,
		body: MultiTenantOrganization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MultiTenantOrganization:
		"""
		Update multiTenantOrganization
		Update the properties of a multi-tenant organization.
		Find more info here: https://learn.microsoft.com/graph/api/multitenantorganization-update?view=graph-rest-beta
		"""
		tags = ['tenantRelationships.multiTenantOrganization']

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
		return await self.request_adapter.send_async(request_info, MultiTenantOrganization, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MultiTenantOrganizationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MultiTenantOrganizationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MultiTenantOrganizationRequest(self.request_adapter, self.path_parameters)

	@property
	def join_request(self,
	) -> JoinRequestRequest:
		from .join_request import JoinRequestRequest
		return JoinRequestRequest(self.request_adapter, self.path_parameters)

	@property
	def tenants(self,
	) -> TenantsRequest:
		from .tenants import TenantsRequest
		return TenantsRequest(self.request_adapter, self.path_parameters)

