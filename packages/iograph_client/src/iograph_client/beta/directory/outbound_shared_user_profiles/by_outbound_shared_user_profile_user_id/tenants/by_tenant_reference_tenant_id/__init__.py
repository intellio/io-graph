# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .remove_personal_data import RemovePersonalDataRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.tenant_reference import TenantReference
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByTenantReferenceTenantIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/outboundSharedUserProfiles/{outboundSharedUserProfile%2DuserId}/tenants/{tenantReference%2DtenantId}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TenantReference:
		"""
		Get tenants from directory
		The collection of external Microsoft Entra tenants that the user shared profile data with. Read-only.
		"""
		tags = ['directory.outboundSharedUserProfile']

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
		return await self.request_adapter.send_async(request_info, TenantReference, error_mapping)

	async def patch(
		self,
		body: TenantReference,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TenantReference:
		"""
		Update the navigation property tenants in directory
		
		"""
		tags = ['directory.outboundSharedUserProfile']

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
		return await self.request_adapter.send_async(request_info, TenantReference, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property tenants for directory
		
		"""
		tags = ['directory.outboundSharedUserProfile']
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



	def with_url(self, raw_url: str) -> ByTenantReferenceTenantIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTenantReferenceTenantIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTenantReferenceTenantIdRequest(self.request_adapter, self.path_parameters)

	def remove_personal_data(self,
		outboundSharedUserProfile_userId: str,
		tenantReference_tenantId: str,
	) -> RemovePersonalDataRequest:
		if outboundSharedUserProfile_userId is None:
			raise TypeError("outboundSharedUserProfile_userId cannot be null.")
		if tenantReference_tenantId is None:
			raise TypeError("tenantReference_tenantId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outboundSharedUserProfile%2DuserId"] =  outboundSharedUserProfile_userId
		path_parameters["tenantReference%2DtenantId"] =  tenantReference_tenantId

		from .remove_personal_data import RemovePersonalDataRequest
		return RemovePersonalDataRequest(self.request_adapter, path_parameters)

