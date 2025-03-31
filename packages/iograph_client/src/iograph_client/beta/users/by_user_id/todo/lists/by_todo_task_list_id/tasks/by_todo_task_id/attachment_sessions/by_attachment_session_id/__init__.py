# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .content import ContentRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.attachment_session import AttachmentSession
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByAttachmentSessionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/todo/lists/{todoTaskList%2Did}/tasks/{todoTask%2Did}/attachmentSessions/{attachmentSession%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttachmentSession:
		"""
		Get attachmentSessions from users
		
		"""
		tags = ['users.todo']

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
		return await self.request_adapter.send_async(request_info, AttachmentSession, error_mapping)

	async def patch(
		self,
		body: AttachmentSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AttachmentSession:
		"""
		Update the navigation property attachmentSessions in users
		
		"""
		tags = ['users.todo']

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
		return await self.request_adapter.send_async(request_info, AttachmentSession, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property attachmentSessions for users
		
		"""
		tags = ['users.todo']
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



	def with_url(self, raw_url: str) -> ByAttachmentSessionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAttachmentSessionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAttachmentSessionIdRequest(self.request_adapter, self.path_parameters)

	def content(self,
		user_id: str,
		todoTaskList_id: str,
		todoTask_id: str,
		attachmentSession_id: str,
	) -> ContentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if todoTaskList_id is None:
			raise TypeError("todoTaskList_id cannot be null.")
		if todoTask_id is None:
			raise TypeError("todoTask_id cannot be null.")
		if attachmentSession_id is None:
			raise TypeError("attachmentSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["todoTaskList%2Did"] =  todoTaskList_id
		path_parameters["todoTask%2Did"] =  todoTask_id
		path_parameters["attachmentSession%2Did"] =  attachmentSession_id

		from .content import ContentRequest
		return ContentRequest(self.request_adapter, path_parameters)

