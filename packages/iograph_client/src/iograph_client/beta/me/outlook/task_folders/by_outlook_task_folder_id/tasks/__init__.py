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
	from .count import CountRequest
	from .by_outlook_task_id import ByOutlookTaskIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.outlook_task_collection_response import OutlookTaskCollectionResponse
from iograph_models.beta.outlook_task import OutlookTask


class TasksRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/outlook/taskFolders/{outlookTaskFolder%2Did}/tasks", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookTaskCollectionResponse:
		"""
		List tasks (deprecated)
		Get all the Outlook tasks in the specified folder. By default, this operation (and the POST, PATCH, and complete task operations) returns
date-related properties in UTC.  You can use a Prefer: outlook.timezone request header to have all the date-related properties in the response represented in a time zone
different than UTC. See an example for getting a single task. You can apply the header similarly to get multiple tasks. If there is more than one task group, and you want to get all the tasks in a specific task group, first
get all the task folders in that task group,
and then get the tasks in each of these task folders.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktaskfolder-list-tasks?view=graph-rest-beta
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
		Create outlookTask (deprecated)
		Create an Outlook task in the specified task folder. The POST method always ignores the time portion of startDateTime and dueDateTime in the request body, and assumes the time 
to be always midnight in the specified time zone.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktaskfolder-post-tasks?view=graph-rest-beta
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
		outlookTaskFolder_id: str,
		outlookTask_id: str,
	) -> ByOutlookTaskIdRequest:
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .by_outlook_task_id import ByOutlookTaskIdRequest
		return ByOutlookTaskIdRequest(self.request_adapter, path_parameters)

	def count(self,
		outlookTaskFolder_id: str,
	) -> CountRequest:
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

