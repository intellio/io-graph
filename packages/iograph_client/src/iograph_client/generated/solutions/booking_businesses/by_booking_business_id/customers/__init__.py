# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_booking_customer_base_id import ByBookingCustomerBaseIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.booking_customer_base_collection_response import BookingCustomerBaseCollectionResponse
from iograph_models.models.booking_customer_base import BookingCustomerBase
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CustomersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}/customers", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BookingCustomerBaseCollectionResponse:
		"""
		List customers
		Get a list of bookingCustomer objects of a business.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-list-customers?view=graph-rest-1.0
		"""
		tags = ['solutions.bookingBusiness']

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
		return await self.request_adapter.send_async(request_info, BookingCustomerBaseCollectionResponse, error_mapping)

	async def post(
		self,
		body: BookingCustomerBase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BookingCustomerBase:
		"""
		Create bookingCustomer
		Create a new bookingCustomer object.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-post-customers?view=graph-rest-1.0
		"""
		tags = ['solutions.bookingBusiness']

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
		return await self.request_adapter.send_async(request_info, BookingCustomerBase, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CustomersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CustomersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CustomersRequest(self.request_adapter, self.path_parameters)

	def by_booking_customer_base_id(self,
		bookingBusiness_id: str,
		bookingCustomerBase_id: str,
	) -> ByBookingCustomerBaseIdRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")
		if bookingCustomerBase_id is None:
			raise TypeError("bookingCustomerBase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id
		path_parameters["bookingCustomerBase%2Did"] =  bookingCustomerBase_id

		from .by_booking_customer_base_id import ByBookingCustomerBaseIdRequest
		return ByBookingCustomerBaseIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

