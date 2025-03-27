# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .industry_data_reset import IndustryDataResetRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.industry_data_provisioning_flow import IndustryDataProvisioningFlow
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByProvisioningFlowIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/industryData/outboundProvisioningFlowSets/{outboundProvisioningFlowSet%2Did}/provisioningFlows/{provisioningFlow%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IndustryDataProvisioningFlow:
		"""
		Get provisioningFlows from external
		A flow that provisions relevant records of a given entity type in the Microsoft 365 tenant.
		"""
		tags = ['external.industryDataRoot']

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
		return await self.request_adapter.send_async(request_info, IndustryDataProvisioningFlow, error_mapping)

	async def patch(
		self,
		body: IndustryDataProvisioningFlow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IndustryDataProvisioningFlow:
		"""
		Update the navigation property provisioningFlows in external
		
		"""
		tags = ['external.industryDataRoot']

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
		return await self.request_adapter.send_async(request_info, IndustryDataProvisioningFlow, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property provisioningFlows for external
		
		"""
		tags = ['external.industryDataRoot']
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



	def with_url(self, raw_url: str) -> ByProvisioningFlowIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByProvisioningFlowIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByProvisioningFlowIdRequest(self.request_adapter, self.path_parameters)

	def industry_data_reset(self,
		outboundProvisioningFlowSet_id: str,
		provisioningFlow_id: str,
	) -> IndustryDataResetRequest:
		if outboundProvisioningFlowSet_id is None:
			raise TypeError("outboundProvisioningFlowSet_id cannot be null.")
		if provisioningFlow_id is None:
			raise TypeError("provisioningFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outboundProvisioningFlowSet%2Did"] =  outboundProvisioningFlowSet_id
		path_parameters["provisioningFlow%2Did"] =  provisioningFlow_id

		from .industry_data_reset import IndustryDataResetRequest
		return IndustryDataResetRequest(self.request_adapter, path_parameters)

