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
	from .shipment_method import ShipmentMethodRequest
	from .picture import PictureRequest
	from .payment_term import PaymentTermRequest
	from .payment_method import PaymentMethodRequest
	from .currency import CurrencyRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.customer import Customer
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCustomerIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/customers/{customer%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Customer:
		"""
		Get customers from financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, Customer, error_mapping)

	async def patch(
		self,
		body: Customer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Customer:
		"""
		Update the navigation property customers in financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, Customer, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property customers for financials
		
		"""
		tags = ['financials.company']
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



	def with_url(self, raw_url: str) -> ByCustomerIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCustomerIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCustomerIdRequest(self.request_adapter, self.path_parameters)

	def currency(self,
		company_id: UUID,
		customer_id: UUID,
	) -> CurrencyRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if customer_id is None:
			raise TypeError("customer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["customer%2Did"] =  customer_id

		from .currency import CurrencyRequest
		return CurrencyRequest(self.request_adapter, path_parameters)

	def payment_method(self,
		company_id: UUID,
		customer_id: UUID,
	) -> PaymentMethodRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if customer_id is None:
			raise TypeError("customer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["customer%2Did"] =  customer_id

		from .payment_method import PaymentMethodRequest
		return PaymentMethodRequest(self.request_adapter, path_parameters)

	def payment_term(self,
		company_id: UUID,
		customer_id: UUID,
	) -> PaymentTermRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if customer_id is None:
			raise TypeError("customer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["customer%2Did"] =  customer_id

		from .payment_term import PaymentTermRequest
		return PaymentTermRequest(self.request_adapter, path_parameters)

	def picture(self,
		company_id: UUID,
		customer_id: UUID,
	) -> PictureRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if customer_id is None:
			raise TypeError("customer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["customer%2Did"] =  customer_id

		from .picture import PictureRequest
		return PictureRequest(self.request_adapter, path_parameters)

	def shipment_method(self,
		company_id: UUID,
		customer_id: UUID,
	) -> ShipmentMethodRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if customer_id is None:
			raise TypeError("customer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["customer%2Did"] =  customer_id

		from .shipment_method import ShipmentMethodRequest
		return ShipmentMethodRequest(self.request_adapter, path_parameters)

