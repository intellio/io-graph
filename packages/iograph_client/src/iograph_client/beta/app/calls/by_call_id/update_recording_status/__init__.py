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
from iograph_models.beta.update_recording_status_post_request import Update_recording_statusPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.update_recording_status_operation import UpdateRecordingStatusOperation


class UpdateRecordingStatusRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/app/calls/{call%2Did}/updateRecordingStatus", path_parameters)

	async def post(
		self,
		body: Update_recording_statusPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UpdateRecordingStatusOperation:
		"""
		Invoke action updateRecordingStatus
		Update the application's recording status associated with a call. This requires the use of the Teams policy-based recording solution.
		Find more info here: https://learn.microsoft.com/graph/api/call-updaterecordingstatus?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, UpdateRecordingStatusOperation, error_mapping)


	def with_url(self, raw_url: str) -> UpdateRecordingStatusRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UpdateRecordingStatusRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UpdateRecordingStatusRequest(self.request_adapter, self.path_parameters)

