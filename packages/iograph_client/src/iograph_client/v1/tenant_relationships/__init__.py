# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .multi_tenant_organization import MultiTenantOrganizationRequest
	from .find_tenant_information_by_tenant_id_with_tenantid import FindTenantInformationByTenantIdWithTenantIdRequest
	from .find_tenant_information_by_domain_name_with_domainname import FindTenantInformationByDomainNameWithDomainNameRequest
	from .delegated_admin_relationships import DelegatedAdminRelationshipsRequest
	from .delegated_admin_customers import DelegatedAdminCustomersRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.tenant_relationship import TenantRelationship
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class TenantRelationshipsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TenantRelationship:
		"""
		Get tenantRelationships
		
		"""
		tags = ['tenantRelationships.tenantRelationship']

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
		return await self.request_adapter.send_async(request_info, TenantRelationship, error_mapping)

	async def patch(
		self,
		body: TenantRelationship,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TenantRelationship:
		"""
		Update tenantRelationships
		
		"""
		tags = ['tenantRelationships.tenantRelationship']

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
		return await self.request_adapter.send_async(request_info, TenantRelationship, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TenantRelationshipsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TenantRelationshipsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TenantRelationshipsRequest(self.request_adapter, self.path_parameters)

	@property
	def delegated_admin_customers(self,
	) -> DelegatedAdminCustomersRequest:
		from .delegated_admin_customers import DelegatedAdminCustomersRequest
		return DelegatedAdminCustomersRequest(self.request_adapter, self.path_parameters)

	@property
	def delegated_admin_relationships(self,
	) -> DelegatedAdminRelationshipsRequest:
		from .delegated_admin_relationships import DelegatedAdminRelationshipsRequest
		return DelegatedAdminRelationshipsRequest(self.request_adapter, self.path_parameters)

	def find_tenant_information_by_domain_name_with_domainname(self,
		domainName: str,
	) -> FindTenantInformationByDomainNameWithDomainNameRequest:
		if domainName is None:
			raise TypeError("domainName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domainName"] =  domainName

		from .find_tenant_information_by_domain_name_with_domainname import FindTenantInformationByDomainNameWithDomainNameRequest
		return FindTenantInformationByDomainNameWithDomainNameRequest(self.request_adapter, path_parameters)

	def find_tenant_information_by_tenant_id_with_tenantid(self,
		tenantId: str,
	) -> FindTenantInformationByTenantIdWithTenantIdRequest:
		if tenantId is None:
			raise TypeError("tenantId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["tenantId"] =  tenantId

		from .find_tenant_information_by_tenant_id_with_tenantid import FindTenantInformationByTenantIdWithTenantIdRequest
		return FindTenantInformationByTenantIdWithTenantIdRequest(self.request_adapter, path_parameters)

	@property
	def multi_tenant_organization(self,
	) -> MultiTenantOrganizationRequest:
		from .multi_tenant_organization import MultiTenantOrganizationRequest
		return MultiTenantOrganizationRequest(self.request_adapter, self.path_parameters)

