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
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.find_meeting_times_response import FindMeetingTimesResponse
from iograph_models.beta.find_meeting_times_post_request import Find_meeting_timesPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class FindMeetingTimesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/findMeetingTimes", path_parameters)

	async def post(
		self,
		body: Find_meeting_timesPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FindMeetingTimesResponse:
		"""
		Invoke action findMeetingTimes
		Suggest meeting times and locations based on organizer and attendee availability, and time or location constraints specified as parameters. If findMeetingTimes cannot return any meeting suggestions, the response would indicate a reason in the emptySuggestionsReason property.
Based on this value, you can better adjust the parameters and call findMeetingTimes again. The algorithm used to suggest meeting times and locations undergoes fine-tuning from time to time. In scenarios like test environments where the input parameters and calendar data remain static, expect that the suggested results may differ over time.
		Find more info here: https://learn.microsoft.com/graph/api/user-findmeetingtimes?view=graph-rest-beta
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


	def with_url(self, raw_url: str) -> FindMeetingTimesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FindMeetingTimesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FindMeetingTimesRequest(self.request_adapter, self.path_parameters)

