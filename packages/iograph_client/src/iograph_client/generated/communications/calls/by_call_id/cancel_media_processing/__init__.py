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
from iograph_models.models.cancel_media_processing_operation import CancelMediaProcessingOperation
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.cancel_media_processing_post_request import Cancel_media_processingPostRequest


class CancelMediaProcessingRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/cancelMediaProcessing", path_parameters)

	async def post(
		self,
		body: Cancel_media_processingPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CancelMediaProcessingOperation:
		"""
		Invoke action cancelMediaProcessing
		Cancels processing for any in-progress media operations. Media operations refer to the IVR operations playPrompt and recordResponse, which are by default queued to process in order. The cancelMediaProcessing method cancels any operation that is in-process as well as operations that are queued. For example, this method can be used to clean up the IVR operation queue for a new media operation. However, it will not cancel a subscribeToTone operation because it operates independent of any operation queue.
		Find more info here: https://learn.microsoft.com/graph/api/call-cancelmediaprocessing?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CancelMediaProcessingOperation, error_mapping)


	def with_url(self, raw_url: str) -> CancelMediaProcessingRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CancelMediaProcessingRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CancelMediaProcessingRequest(self.request_adapter, self.path_parameters)

