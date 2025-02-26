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
from iograph_models.models.cancel_media_processing_operation import CancelMediaProcessingOperation
from iograph_models.models.cancel_media_processing_post_request import Cancel_media_processingPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CancelMediaProcessingRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/cancelMediaProcessing"
		self.path_parameters: dict[str, Any] = path_parameters

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


