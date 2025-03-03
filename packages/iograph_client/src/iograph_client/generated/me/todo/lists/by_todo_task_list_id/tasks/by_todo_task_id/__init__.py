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
	from .linked_resources import LinkedResourcesRequest
	from .extensions import ExtensionsRequest
	from .checklist_items import ChecklistItemsRequest
	from .attachment_sessions import AttachmentSessionsRequest
	from .attachments import AttachmentsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.todo_task import TodoTask
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByTodoTaskIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/todo/lists/{todoTaskList%2Did}/tasks/{todoTask%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TodoTask:
		"""
		Get todoTask
		Read the properties and relationships of a todoTask object.
		Find more info here: https://learn.microsoft.com/graph/api/todotask-get?view=graph-rest-1.0
		"""
		tags = ['me.todo']

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
		return await self.request_adapter.send_async(request_info, TodoTask, error_mapping)

	async def patch(
		self,
		body: TodoTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TodoTask:
		"""
		Update todoTask
		Update the properties of a todoTask object.
		Find more info here: https://learn.microsoft.com/graph/api/todotask-update?view=graph-rest-1.0
		"""
		tags = ['me.todo']

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
		return await self.request_adapter.send_async(request_info, TodoTask, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete todoTask
		Deletes a todoTask object.
		Find more info here: https://learn.microsoft.com/graph/api/todotask-delete?view=graph-rest-1.0
		"""
		tags = ['me.todo']
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



	def with_url(self, raw_url: str) -> ByTodoTaskIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTodoTaskIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTodoTaskIdRequest(self.request_adapter, self.path_parameters)

	@property
	def attachments(self,
	) -> AttachmentsRequest:
		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def attachment_sessions(self,
	) -> AttachmentSessionsRequest:
		from .attachment_sessions import AttachmentSessionsRequest
		return AttachmentSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def checklist_items(self,
	) -> ChecklistItemsRequest:
		from .checklist_items import ChecklistItemsRequest
		return ChecklistItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def extensions(self,
	) -> ExtensionsRequest:
		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def linked_resources(self,
	) -> LinkedResourcesRequest:
		from .linked_resources import LinkedResourcesRequest
		return LinkedResourcesRequest(self.request_adapter, self.path_parameters)

