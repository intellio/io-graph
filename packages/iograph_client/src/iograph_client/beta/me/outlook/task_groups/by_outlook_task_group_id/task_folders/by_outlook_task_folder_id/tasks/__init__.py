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
	from .count import CountRequest
	from .by_outlook_task_id import ByOutlookTaskIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.outlook_task_collection_response import OutlookTaskCollectionResponse
from iograph_models.beta.outlook_task import OutlookTask


class TasksRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/outlook/taskGroups/{outlookTaskGroup%2Did}/taskFolders/{outlookTaskFolder%2Did}/tasks", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookTaskCollectionResponse:
		"""
		Get tasks from me
		The tasks in this task folder. Read-only. Nullable.
		"""
		tags = ['me.outlookUser']

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
		return await self.request_adapter.send_async(request_info, OutlookTaskCollectionResponse, error_mapping)

	async def post(
		self,
		body: OutlookTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OutlookTask:
		"""
		Create new navigation property to tasks for me
		
		"""
		tags = ['me.outlookUser']

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
		return await self.request_adapter.send_async(request_info, OutlookTask, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TasksRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TasksRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TasksRequest(self.request_adapter, self.path_parameters)

	def by_outlook_task_id(self,
		outlookTaskGroup_id: str,
		outlookTaskFolder_id: str,
		outlookTask_id: str,
	) -> ByOutlookTaskIdRequest:
		if outlookTaskGroup_id is None:
			raise TypeError("outlookTaskGroup_id cannot be null.")
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskGroup%2Did"] =  outlookTaskGroup_id
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .by_outlook_task_id import ByOutlookTaskIdRequest
		return ByOutlookTaskIdRequest(self.request_adapter, path_parameters)

	def count(self,
		outlookTaskGroup_id: str,
		outlookTaskFolder_id: str,
	) -> CountRequest:
		if outlookTaskGroup_id is None:
			raise TypeError("outlookTaskGroup_id cannot be null.")
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskGroup%2Did"] =  outlookTaskGroup_id
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

