# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.record_operation import RecordOperation
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.record_response_post_request import Record_responsePostRequest


class RecordResponseRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/app/calls/{call%2Did}/recordResponse", path_parameters)

	async def post(
		self,
		body: Record_responsePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RecordOperation:
		"""
		Invoke action recordResponse
		Record a short audio response from the caller. A bot can use this API to capture a voice response from a caller after they're prompted for a response. For more information about how to handle operations, see commsOperation. This action isn't intended to record the entire call. The maximum length of recording is 2 minutes.The Cloud Communications Platform doesn't save the recording permanently and discards it shortly after the call ends. The bot must download the recording promptly after the recording operation finishes by using the recordingLocation value provided in the completed notification.
		Find more info here: https://learn.microsoft.com/graph/api/call-record?view=graph-rest-beta
		"""
		tags = ['app.call']

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
		return await self.request_adapter.send_async(request_info, RecordOperation, error_mapping)


	def with_url(self, raw_url: str) -> RecordResponseRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RecordResponseRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RecordResponseRequest(self.request_adapter, self.path_parameters)

