# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.booking_service import BookingService
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByBookingServiceIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}/services/{bookingService%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BookingService:
		"""
		Get bookingService
		Get the properties and relationships of a bookingService object in the specified bookingBusiness.
		Find more info here: https://learn.microsoft.com/graph/api/bookingservice-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, BookingService, error_mapping)

	async def patch(
		self,
		body: BookingService,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BookingService:
		"""
		Update bookingservice
		Update the properties of a bookingService object in the specified bookingBusiness. The following are some examples you can customize for a service:
- Price
- Typical length of an appointment
- Reminders
- Any time buffer to set up before or finish up after the service
- Scheduling policy parameters, such as minimum notice to book or cancel, and whether customers can select specific staff members for an appointment.
		Find more info here: https://learn.microsoft.com/graph/api/bookingservice-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, BookingService, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete bookingService
		Delete a bookingService object in the specified bookingBusiness.
		Find more info here: https://learn.microsoft.com/graph/api/bookingservice-delete?view=graph-rest-1.0
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



