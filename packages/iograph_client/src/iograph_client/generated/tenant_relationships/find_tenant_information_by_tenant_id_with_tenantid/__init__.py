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
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.tenant_information import TenantInformation


class FindTenantInformationByTenantIdWithTenantIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/tenantRelationships/findTenantInformationByTenantId(tenantId='{tenantId}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TenantInformation:
		"""
		Invoke function findTenantInformationByTenantId
		Given a tenant ID, search for a tenant and read its tenantInformation. You can use this API to validate tenant information and use the tenantId to configure cross-tenant cross-tenant access settings between you and the tenant.
		Find more info here: https://learn.microsoft.com/graph/api/tenantrelationship-findtenantinformationbytenantid?view=graph-rest-1.0
		"""
		tags = ['tenantRelationships.tenantRelationship.Functions']

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
		return await self.request_adapter.send_async(request_info, TenantInformation, error_mapping)


	def with_url(self, raw_url: str) -> FindTenantInformationByTenantIdWithTenantIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FindTenantInformationByTenantIdWithTenantIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FindTenantInformationByTenantIdWithTenantIdRequest(self.request_adapter, self.path_parameters)

