# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_booking_service_id import ByBookingServiceIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.booking_service import BookingService
from iograph_models.beta.booking_service_collection_response import BookingServiceCollectionResponse


class ServicesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/bookingBusinesses/{bookingBusiness%2Did}/services", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BookingServiceCollectionResponse:
		"""
		Get services from bookingBusinesses
		All the services offered by this business. Read-only. Nullable.
		"""
		tags = ['bookingBusinesses.bookingService']

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
		return await self.request_adapter.send_async(request_info, BookingServiceCollectionResponse, error_mapping)

	async def post(
		self,
		body: BookingService,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BookingService:
		"""
		Create new navigation property to services for bookingBusinesses
		
		"""
		tags = ['bookingBusinesses.bookingService']

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
		return await self.request_adapter.send_async(request_info, BookingService, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ServicesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ServicesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ServicesRequest(self.request_adapter, self.path_parameters)

	def by_booking_service_id(self,
		bookingBusiness_id: str,
		bookingService_id: str,
	) -> ByBookingServiceIdRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")
		if bookingService_id is None:
			raise TypeError("bookingService_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id
		path_parameters["bookingService%2Did"] =  bookingService_id

		from .by_booking_service_id import ByBookingServiceIdRequest
		return ByBookingServiceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		bookingBusiness_id: str,
	) -> CountRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

