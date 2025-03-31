# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .item_at_with_index import ItemAtWithIndexRequest
	from .count import CountRequest
	from .by_workbook_document_task_change_id import ByWorkbookDocumentTaskChangeIdRequest
	from ...............request_adapter import HttpxRequestAdapter
from iograph_models.beta.workbook_document_task_change_collection_response import WorkbookDocumentTaskChangeCollectionResponse
from iograph_models.beta.workbook_document_task_change import WorkbookDocumentTaskChange
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ChangesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/comments/{workbookComment%2Did}/replies/{workbookCommentReply%2Did}/task/comment/task/changes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookDocumentTaskChangeCollectionResponse:
		"""
		Get changes from drives
		A collection of task change histories.
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
		return await self.request_adapter.send_async(request_info, WorkbookDocumentTaskChangeCollectionResponse, error_mapping)

	async def post(
		self,
		body: WorkbookDocumentTaskChange,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookDocumentTaskChange:
		"""
		Create new navigation property to changes for drives
		
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookDocumentTaskChange, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ChangesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChangesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChangesRequest(self.request_adapter, self.path_parameters)

	def by_workbook_document_task_change_id(self,
		drive_id: str,
		driveItem_id: str,
		workbookComment_id: str,
		workbookCommentReply_id: str,
		workbookDocumentTaskChange_id: str,
	) -> ByWorkbookDocumentTaskChangeIdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookComment_id is None:
			raise TypeError("workbookComment_id cannot be null.")
		if workbookCommentReply_id is None:
			raise TypeError("workbookCommentReply_id cannot be null.")
		if workbookDocumentTaskChange_id is None:
			raise TypeError("workbookDocumentTaskChange_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookComment%2Did"] =  workbookComment_id
		path_parameters["workbookCommentReply%2Did"] =  workbookCommentReply_id
		path_parameters["workbookDocumentTaskChange%2Did"] =  workbookDocumentTaskChange_id

		from .by_workbook_document_task_change_id import ByWorkbookDocumentTaskChangeIdRequest
		return ByWorkbookDocumentTaskChangeIdRequest(self.request_adapter, path_parameters)

	def count(self,
		drive_id: str,
		driveItem_id: str,
		workbookComment_id: str,
		workbookCommentReply_id: str,
	) -> CountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookComment_id is None:
			raise TypeError("workbookComment_id cannot be null.")
		if workbookCommentReply_id is None:
			raise TypeError("workbookCommentReply_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookComment%2Did"] =  workbookComment_id
		path_parameters["workbookCommentReply%2Did"] =  workbookCommentReply_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def item_at_with_index(self,
		drive_id: str,
		driveItem_id: str,
		workbookComment_id: str,
		workbookCommentReply_id: str,
		index: int,
	) -> ItemAtWithIndexRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookComment_id is None:
			raise TypeError("workbookComment_id cannot be null.")
		if workbookCommentReply_id is None:
			raise TypeError("workbookCommentReply_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookComment%2Did"] =  workbookComment_id
		path_parameters["workbookCommentReply%2Did"] =  workbookCommentReply_id
		path_parameters["index"] =  index

		from .item_at_with_index import ItemAtWithIndexRequest
		return ItemAtWithIndexRequest(self.request_adapter, path_parameters)

