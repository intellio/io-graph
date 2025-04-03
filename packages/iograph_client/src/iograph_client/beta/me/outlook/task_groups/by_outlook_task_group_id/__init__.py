# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .task_folders import TaskFoldersRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.outlook_task_group import OutlookTaskGroup
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByOutlookTaskGroupIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/outlook/taskGroups/{outlookTaskGroup%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookTaskGroup:
		"""
		Get outlookTaskGroup (deprecated)
		Get the properties and relationships of the specified Outlook task group.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktaskgroup-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, OutlookTaskGroup, error_mapping)

	async def patch(
		self,
		body: OutlookTaskGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OutlookTaskGroup:
		"""
		Update outlooktaskgroup (deprecated)
		Update the writable properties of an Outlook task group. You can't modify the name of the default task group, 'My Tasks'.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktaskgroup-update?view=graph-rest-beta
		"""
		tags = ['me.outlookUser']

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
		return await self.request_adapter.send_async(request_info, OutlookTaskGroup, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete outlookTaskGroup (deprecated)
		Delete the specified outlookTaskGroup.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktaskgroup-delete?view=graph-rest-beta
		"""
		tags = ['me.outlookUser']
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



	def with_url(self, raw_url: str) -> ByOutlookTaskGroupIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOutlookTaskGroupIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOutlookTaskGroupIdRequest(self.request_adapter, self.path_parameters)

	def task_folders(self,
		outlookTaskGroup_id: str,
	) -> TaskFoldersRequest:
		if outlookTaskGroup_id is None:
			raise TypeError("outlookTaskGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskGroup%2Did"] =  outlookTaskGroup_id

		from .task_folders import TaskFoldersRequest
		return TaskFoldersRequest(self.request_adapter, path_parameters)

