# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .replies import RepliesRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.workbook_comment import WorkbookComment


class ByWorkbookCommentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/comments/{workbookComment%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookComment:
		"""
		Get comments from drives
		Represents a collection of comments in a workbook.
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookComment, error_mapping)

	async def patch(
		self,
		body: WorkbookComment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookComment:
		"""
		Update the navigation property comments in drives
		
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookComment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property comments for drives
		
		"""
		tags = ['drives.driveItem']
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



	def with_url(self, raw_url: str) -> ByWorkbookCommentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWorkbookCommentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWorkbookCommentIdRequest(self.request_adapter, self.path_parameters)

	def replies(self,
		drive_id: str,
		driveItem_id: str,
		workbookComment_id: str,
	) -> RepliesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookComment_id is None:
			raise TypeError("workbookComment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookComment%2Did"] =  workbookComment_id

		from .replies import RepliesRequest
		return RepliesRequest(self.request_adapter, path_parameters)

