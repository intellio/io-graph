# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .png_of_current_slide import PngOfCurrentSlideRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.content_sharing_session import ContentSharingSession
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByContentSharingSessionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/contentSharingSessions/{contentSharingSession%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentSharingSession:
		"""
		Get contentSharingSession
		Retrieve the properties of a contentSharingSession object.
		Find more info here: https://learn.microsoft.com/graph/api/contentsharingsession-get?view=graph-rest-beta
		"""
		tags = ['communications.call']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, ContentSharingSession, error_mapping)

	async def patch(
		self,
		body: ContentSharingSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentSharingSession:
		"""
		Update the navigation property contentSharingSessions in communications
		
		"""
		tags = ['communications.call']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, ContentSharingSession, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property contentSharingSessions for communications
		
		"""
		tags = ['communications.call']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByContentSharingSessionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByContentSharingSessionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByContentSharingSessionIdRequest(self.request_adapter, self.path_parameters)

	def png_of_current_slide(self,
		call_id: str,
		contentSharingSession_id: str,
	) -> PngOfCurrentSlideRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if contentSharingSession_id is None:
			raise TypeError("contentSharingSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["contentSharingSession%2Did"] =  contentSharingSession_id

		from .png_of_current_slide import PngOfCurrentSlideRequest
		return PngOfCurrentSlideRequest(self.request_adapter, path_parameters)

