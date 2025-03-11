# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_tenants_tenant_search_post_response import Managed_tenants_tenant_searchPostResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.managed_tenants_tenant_search_post_request import Managed_tenants_tenant_searchPostRequest


class ManagedTenantsTenantSearchRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/tenantGroups/microsoft.graph.managedTenants.tenantSearch", path_parameters)

	async def post(
		self,
		body: Managed_tenants_tenant_searchPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Managed_tenants_tenant_searchPostResponse:
		"""
		Invoke action tenantSearch
		Searches for the specified managed tenants across tenant groups.
		"""
		tags = ['tenantRelationships.managedTenant']

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
		return await self.request_adapter.send_async(request_info, Managed_tenants_tenant_searchPostResponse, error_mapping)


	def with_url(self, raw_url: str) -> ManagedTenantsTenantSearchRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ManagedTenantsTenantSearchRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ManagedTenantsTenantSearchRequest(self.request_adapter, self.path_parameters)

