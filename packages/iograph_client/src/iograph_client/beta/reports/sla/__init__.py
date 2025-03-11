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
	from .azure_a_d_authentication import AzureADAuthenticationRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.service_level_agreement_root import ServiceLevelAgreementRoot
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SlaRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports/sla", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServiceLevelAgreementRoot:
		"""
		Get sla from reports
		Reports that relate to tenant-level Microsoft Entra Health SLA attainment.
		"""
		tags = ['reports.serviceLevelAgreementRoot']

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
		return await self.request_adapter.send_async(request_info, ServiceLevelAgreementRoot, error_mapping)

	async def patch(
		self,
		body: ServiceLevelAgreementRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServiceLevelAgreementRoot:
		"""
		Update the navigation property sla in reports
		
		"""
		tags = ['reports.serviceLevelAgreementRoot']

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
		return await self.request_adapter.send_async(request_info, ServiceLevelAgreementRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sla for reports
		
		"""
		tags = ['reports.serviceLevelAgreementRoot']
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



	def with_url(self, raw_url: str) -> SlaRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SlaRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SlaRequest(self.request_adapter, self.path_parameters)

	@property
	def azure_a_d_authentication(self,
	) -> AzureADAuthenticationRequest:
		from .azure_a_d_authentication import AzureADAuthenticationRequest
		return AzureADAuthenticationRequest(self.request_adapter, self.path_parameters)

