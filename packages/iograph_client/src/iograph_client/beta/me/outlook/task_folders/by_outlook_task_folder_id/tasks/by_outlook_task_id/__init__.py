# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .permanent_delete import PermanentDeleteRequest
	from .complete import CompleteRequest
	from .attachments import AttachmentsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.outlook_task import OutlookTask


class ByOutlookTaskIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/outlook/taskFolders/{outlookTaskFolder%2Did}/tasks/{outlookTask%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookTask:
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
		return await self.request_adapter.send_async(request_info, OutlookTask, error_mapping)

	async def patch(
		self,
		body: OutlookTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OutlookTask:
		"""
		Update the navigation property tasks in me
		
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
		return await self.request_adapter.send_async(request_info, OutlookTask, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property tasks for me
		
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



	def with_url(self, raw_url: str) -> ByOutlookTaskIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOutlookTaskIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOutlookTaskIdRequest(self.request_adapter, self.path_parameters)

	def attachments(self,
		outlookTaskFolder_id: str,
		outlookTask_id: str,
	) -> AttachmentsRequest:
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def complete(self,
		outlookTaskFolder_id: str,
		outlookTask_id: str,
	) -> CompleteRequest:
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .complete import CompleteRequest
		return CompleteRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		outlookTaskFolder_id: str,
		outlookTask_id: str,
	) -> PermanentDeleteRequest:
		if outlookTaskFolder_id is None:
			raise TypeError("outlookTaskFolder_id cannot be null.")
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTaskFolder%2Did"] =  outlookTaskFolder_id
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

