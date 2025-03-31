# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_checklist_item_id import ByChecklistItemIdRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.checklist_item import ChecklistItem
from iograph_models.beta.checklist_item_collection_response import ChecklistItemCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ChecklistItemsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/todo/lists/{todoTaskList%2Did}/tasks/{todoTask%2Did}/checklistItems", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChecklistItemCollectionResponse:
		"""
		Get checklistItems from users
		A collection of smaller subtasks linked to the more complex parent task.
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
		return await self.request_adapter.send_async(request_info, ChecklistItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: ChecklistItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ChecklistItem:
		"""
		Create new navigation property to checklistItems for users
		
		"""
		tags = ['users.todo']

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
		return await self.request_adapter.send_async(request_info, ChecklistItem, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ChecklistItemsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChecklistItemsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChecklistItemsRequest(self.request_adapter, self.path_parameters)

	def by_checklist_item_id(self,
		user_id: str,
		todoTaskList_id: str,
		todoTask_id: str,
		checklistItem_id: str,
	) -> ByChecklistItemIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if todoTaskList_id is None:
			raise TypeError("todoTaskList_id cannot be null.")
		if todoTask_id is None:
			raise TypeError("todoTask_id cannot be null.")
		if checklistItem_id is None:
			raise TypeError("checklistItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["todoTaskList%2Did"] =  todoTaskList_id
		path_parameters["todoTask%2Did"] =  todoTask_id
		path_parameters["checklistItem%2Did"] =  checklistItem_id

		from .by_checklist_item_id import ByChecklistItemIdRequest
		return ByChecklistItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		todoTaskList_id: str,
		todoTask_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if todoTaskList_id is None:
			raise TypeError("todoTaskList_id cannot be null.")
		if todoTask_id is None:
			raise TypeError("todoTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["todoTaskList%2Did"] =  todoTaskList_id
		path_parameters["todoTask%2Did"] =  todoTask_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

