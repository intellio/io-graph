# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.answer_post_request import AnswerPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class AnswerRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/answer"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: AnswerPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action answer
		Enable a bot to answer an incoming call. The incoming call request can be an invitation from a participant in a group call or a peer-to-peer call. If an invitation to a group call is received, the notification contains the chatInfo and meetingInfo parameters. The bot is expected to answer, reject, or redirect the call before the call times out. The current timeout value is 15 seconds for regular scenarios and 5 seconds for policy-based recording scenarios. This API supports the following PSTN scenarios:
		Find more info here: https://learn.microsoft.com/graph/api/call-answer?view=graph-rest-1.0
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


