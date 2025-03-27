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
from iograph_models.beta.add_large_gallery_view_operation import AddLargeGalleryViewOperation
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.add_large_gallery_view_post_request import Add_large_gallery_viewPostRequest


class AddLargeGalleryViewRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/addLargeGalleryView", path_parameters)

	async def post(
		self,
		body: Add_large_gallery_viewPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AddLargeGalleryViewOperation:
		"""
		Invoke action addLargeGalleryView
		Add the large gallery view to a call.  For details about how to identify a large gallery view participant in a roster so that you can retrieve the relevant data to subscribe to the video feed, see Identify large gallery view participants in a roster.
		Find more info here: https://learn.microsoft.com/graph/api/call-addlargegalleryview?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, AddLargeGalleryViewOperation, error_mapping)


	def with_url(self, raw_url: str) -> AddLargeGalleryViewRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AddLargeGalleryViewRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AddLargeGalleryViewRequest(self.request_adapter, self.path_parameters)

