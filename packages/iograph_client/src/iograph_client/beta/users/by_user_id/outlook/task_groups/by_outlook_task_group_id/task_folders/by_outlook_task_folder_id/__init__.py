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
	from .tasks import TasksRequest
	from .permanent_delete import PermanentDeleteRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.outlook_task_folder import OutlookTaskFolder


class ByOutlookTaskFolderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/outlook/taskGroups/{outlookTaskGroup%2Did}/taskFolders/{outlookTaskFolder%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookTaskFolder:
		"""
		Get taskFolders from users
		The collection of task folders in the task group. Read-only. Nullable.
		"""
		tags = ['users.outlookUser']

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
		return await self.request_adapter.send_async(request_info, OutlookTaskFolder, error_mapping)

	async def patch(
		self,
		body: OutlookTaskFolder,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OutlookTaskFolder:
		"""
		Update the navigation property taskFolders in users
		
		"""
		tags = ['users.outlookUser']

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
		return await self.request_adapter.send_async(request_info, OutlookTaskFolder, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property taskFolders for users
		
		"""
		tags = ['users.outlookUser']
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



	def with_url(self, raw_url: str) -> ByOutlookTaskFolderIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOutlookTaskFolderIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOutlookTaskFolderIdRequest(self.request_adapter, self.path_parameters)

	def permanent_delete(self,
		user_id: str,
		outlookTaskGroup_id: str,
		outlookTaskFolder_id: str,
	) -> PermanentDeleteRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if outlookTaskGroup_id is None:
			raise TypeError("outlookTaskGroup_id cannot be null.")
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["outlookTaskGroup%2Did"] =  outlookTaskGroup_id
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def tasks(self,
		user_id: str,
		outlookTaskGroup_id: str,
		outlookTaskFolder_id: str,
	) -> TasksRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if outlookTaskGroup_id is None:
			raise TypeError("outlookTaskGroup_id cannot be null.")
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["outlookTaskGroup%2Did"] =  outlookTaskGroup_id
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

