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
	from .staff_members import StaffMembersRequest
	from .services import ServicesRequest
	from .unpublish import UnpublishRequest
	from .publish import PublishRequest
	from .get_staff_availability import GetStaffAvailabilityRequest
	from .custom_questions import CustomQuestionsRequest
	from .customers import CustomersRequest
	from .calendar_view import CalendarViewRequest
	from .appointments import AppointmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.booking_business import BookingBusiness


class ByBookingBusinessIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BookingBusiness:
		"""
		Get bookingBusinesses from solutions
		A collection of businesses in Microsoft Bookings. Read-only. Nullable.
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
		return await self.request_adapter.send_async(request_info, BookingBusiness, error_mapping)

	async def patch(
		self,
		body: BookingBusiness,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BookingBusiness:
		"""
		Update the navigation property bookingBusinesses in solutions
		
		"""
		tags = ['solutions.bookingBusiness']

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
		return await self.request_adapter.send_async(request_info, BookingBusiness, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete bookingBusiness
		Delete a bookingBusiness object.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-delete?view=graph-rest-beta
		"""
		tags = ['solutions.bookingBusiness']
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



	def with_url(self, raw_url: str) -> ByBookingBusinessIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByBookingBusinessIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByBookingBusinessIdRequest(self.request_adapter, self.path_parameters)

	def appointments(self,
		bookingBusiness_id: str,
	) -> AppointmentsRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .appointments import AppointmentsRequest
		return AppointmentsRequest(self.request_adapter, path_parameters)

	def calendar_view(self,
		bookingBusiness_id: str,
	) -> CalendarViewRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, path_parameters)

	def customers(self,
		bookingBusiness_id: str,
	) -> CustomersRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .customers import CustomersRequest
		return CustomersRequest(self.request_adapter, path_parameters)

	def custom_questions(self,
		bookingBusiness_id: str,
	) -> CustomQuestionsRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .custom_questions import CustomQuestionsRequest
		return CustomQuestionsRequest(self.request_adapter, path_parameters)

	def get_staff_availability(self,
		bookingBusiness_id: str,
	) -> GetStaffAvailabilityRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .get_staff_availability import GetStaffAvailabilityRequest
		return GetStaffAvailabilityRequest(self.request_adapter, path_parameters)

	def publish(self,
		bookingBusiness_id: str,
	) -> PublishRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, path_parameters)

	def unpublish(self,
		bookingBusiness_id: str,
	) -> UnpublishRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .unpublish import UnpublishRequest
		return UnpublishRequest(self.request_adapter, path_parameters)

	def services(self,
		bookingBusiness_id: str,
	) -> ServicesRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .services import ServicesRequest
		return ServicesRequest(self.request_adapter, path_parameters)

	def staff_members(self,
		bookingBusiness_id: str,
	) -> StaffMembersRequest:
		if bookingBusiness_id is None:
			raise TypeError("bookingBusiness_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["bookingBusiness%2Did"] =  bookingBusiness_id

		from .staff_members import StaffMembersRequest
		return StaffMembersRequest(self.request_adapter, path_parameters)

