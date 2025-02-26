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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.get_schedule_post_request import Get_schedulePostRequest
from iograph_models.models.get_schedule_post_response import Get_schedulePostResponse


class GetScheduleRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/calendars/{calendar%2Did}/getSchedule"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Get_schedulePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Get_schedulePostResponse:
		"""
		Invoke action getSchedule
		Get the free/busy availability information for a collection of users, distributions lists, or resources (rooms or equipment) for a specified time period.
		Find more info here: https://learn.microsoft.com/graph/api/calendar-getschedule?view=graph-rest-1.0
		"""
		tags = ['users.calendar']

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
		return await self.request_adapter.send_async(request_info, Get_schedulePostResponse, error_mapping)


