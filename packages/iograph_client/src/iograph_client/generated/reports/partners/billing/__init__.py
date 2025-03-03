# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .usage import UsageRequest
	from .reconciliation import ReconciliationRequest
	from .operations import OperationsRequest
	from .manifests import ManifestsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.partners_billing_billing import PartnersBillingBilling
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BillingRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports/partners/billing", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PartnersBillingBilling:
		"""
		Get billing from reports
		Represents billing details for billed and unbilled data.
		"""
		tags = ['reports.partners']

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
		return await self.request_adapter.send_async(request_info, PartnersBillingBilling, error_mapping)

	async def patch(
		self,
		body: PartnersBillingBilling,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PartnersBillingBilling:
		"""
		Update the navigation property billing in reports
		
		"""
		tags = ['reports.partners']

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
		return await self.request_adapter.send_async(request_info, PartnersBillingBilling, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property billing for reports
		
		"""
		tags = ['reports.partners']
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



	def with_url(self, raw_url: str) -> BillingRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BillingRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BillingRequest(self.request_adapter, self.path_parameters)

	@property
	def manifests(self,
	) -> ManifestsRequest:
		from .manifests import ManifestsRequest
		return ManifestsRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def reconciliation(self,
	) -> ReconciliationRequest:
		from .reconciliation import ReconciliationRequest
		return ReconciliationRequest(self.request_adapter, self.path_parameters)

	@property
	def usage(self,
	) -> UsageRequest:
		from .usage import UsageRequest
		return UsageRequest(self.request_adapter, self.path_parameters)

