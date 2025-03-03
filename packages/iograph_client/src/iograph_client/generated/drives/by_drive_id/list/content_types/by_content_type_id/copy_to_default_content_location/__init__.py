# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.copy_to_default_content_location_post_request import Copy_to_default_content_locationPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CopyToDefaultContentLocationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/list/contentTypes/{contentType%2Did}/copyToDefaultContentLocation", path_parameters)

	async def post(
		self,
		body: Copy_to_default_content_locationPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action copyToDefaultContentLocation
		Copy a file to a default content location in a content type. The file can then be added as a default file or template via a POST operation.
		Find more info here: https://learn.microsoft.com/graph/api/contenttype-copytodefaultcontentlocation?view=graph-rest-1.0
		"""
		tags = ['drives.list']

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


	def with_url(self, raw_url: str) -> CopyToDefaultContentLocationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CopyToDefaultContentLocationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CopyToDefaultContentLocationRequest(self.request_adapter, self.path_parameters)

