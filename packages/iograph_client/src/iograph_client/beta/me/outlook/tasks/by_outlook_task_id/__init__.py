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
	from .permanent_delete import PermanentDeleteRequest
	from .complete import CompleteRequest
	from .attachments import AttachmentsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.outlook_task import OutlookTask


class ByOutlookTaskIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/outlook/tasks/{outlookTask%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OutlookTask:
		"""
		Get outlookTask (deprecated)
		Get the properties and relationships of an Outlook task in the user's mailbox. By default, this operation (and the POST, PATCH, and complete task operations) returns date-related properties in UTC. You can use the Prefer: outlook.timezone header to have all the date-related properties in the response represented in a time zone different than UTC.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktask-get?view=graph-rest-beta
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
		Update outlooktask (deprecated)
		Change writable properties of an Outlook task. The completedDateTime property can be set by the complete action, or explicitly by a PATCH operation. If you use PATCH to set completedDateTime, make sure you set status to completed as well. By default, this operation (and the POST, GET, and complete task operations) returns date-related properties in UTC. You can use the Prefer: outlook.timezone header to have all the date-related properties in the response represented in a time zone different than UTC.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktask-update?view=graph-rest-beta
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
		Delete outlookTask (deprecated)
		Delete the specified Outlook task in the user's mailbox.
		Find more info here: https://learn.microsoft.com/graph/api/outlooktask-delete?view=graph-rest-beta
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
		outlookTask_id: str,
	) -> AttachmentsRequest:
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def complete(self,
		outlookTask_id: str,
	) -> CompleteRequest:
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .complete import CompleteRequest
		return CompleteRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		outlookTask_id: str,
	) -> PermanentDeleteRequest:
		if outlookTask_id is None:
			raise TypeError("outlookTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["outlookTask%2Did"] =  outlookTask_id

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

