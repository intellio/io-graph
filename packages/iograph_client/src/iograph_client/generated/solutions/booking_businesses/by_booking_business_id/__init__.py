# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.booking_business import BookingBusiness


class ByBookingBusinessIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BookingBusiness:
		"""
		Get bookingBusiness
		Get the properties and relationships of a bookingBusiness object.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-get?view=graph-rest-1.0
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
		Update bookingbusiness
		Update the properties of a bookingBusiness object.
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-update?view=graph-rest-1.0
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
		Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-delete?view=graph-rest-1.0
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



	@property
	def appointments(self,
	) -> AppointmentsRequest:
		from .appointments import AppointmentsRequest
		return AppointmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_view(self,
	) -> CalendarViewRequest:
		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, self.path_parameters)

	@property
	def customers(self,
	) -> CustomersRequest:
		from .customers import CustomersRequest
		return CustomersRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_questions(self,
	) -> CustomQuestionsRequest:
		from .custom_questions import CustomQuestionsRequest
		return CustomQuestionsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_staff_availability(self,
	) -> GetStaffAvailabilityRequest:
		from .get_staff_availability import GetStaffAvailabilityRequest
		return GetStaffAvailabilityRequest(self.request_adapter, self.path_parameters)

	@property
	def publish(self,
	) -> PublishRequest:
		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, self.path_parameters)

	@property
	def unpublish(self,
	) -> UnpublishRequest:
		from .unpublish import UnpublishRequest
		return UnpublishRequest(self.request_adapter, self.path_parameters)

	@property
	def services(self,
	) -> ServicesRequest:
		from .services import ServicesRequest
		return ServicesRequest(self.request_adapter, self.path_parameters)

	@property
	def staff_members(self,
	) -> StaffMembersRequest:
		from .staff_members import StaffMembersRequest
		return StaffMembersRequest(self.request_adapter, self.path_parameters)

