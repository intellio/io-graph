# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.find_meeting_times_response import FindMeetingTimesResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.find_meeting_times_post_request import Find_meeting_timesPostRequest


class FindMeetingTimesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/findMeetingTimes"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Find_meeting_timesPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FindMeetingTimesResponse:
		"""
		Invoke action findMeetingTimes
		Suggest meeting times and locations based on organizer and attendee availability, and time or location constraints specified as parameters. If findMeetingTimes cannot return any meeting suggestions, the response would indicate a reason in the emptySuggestionsReason property.
Based on this value, you can better adjust the parameters and call findMeetingTimes again. The algorithm used to suggest meeting times and locations undergoes fine-tuning from time to time. In scenarios like test environments where the input parameters and calendar data remain static, expect that the suggested results may differ over time.
		Find more info here: https://learn.microsoft.com/graph/api/user-findmeetingtimes?view=graph-rest-1.0
		"""
		tags = ['users.user.Actions']

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
		return await self.request_adapter.send_async(request_info, FindMeetingTimesResponse, error_mapping)


