# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .progress_task_board_format import ProgressTaskBoardFormatRequest
	from .details import DetailsRequest
	from .bucket_task_board_format import BucketTaskBoardFormatRequest
	from .assigned_to_task_board_format import AssignedToTaskBoardFormatRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.planner_task import PlannerTask


class ByPlannerTaskIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/planner/tasks/{plannerTask%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerTask:
		"""
		Get tasks from me
		Read-only. Nullable. Returns the plannerPlans shared with the user.
		"""
		tags = ['me.plannerUser']

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
		return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)

	async def patch(
		self,
		body: PlannerTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerTask:
		"""
		Update the navigation property tasks in me
		
		"""
		tags = ['me.plannerUser']

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
		return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property tasks for me
		
		"""
		tags = ['me.plannerUser']
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



	@property
	def assigned_to_task_board_format(self,
	) -> AssignedToTaskBoardFormatRequest:
		from .assigned_to_task_board_format import AssignedToTaskBoardFormatRequest
		return AssignedToTaskBoardFormatRequest(self.request_adapter, self.path_parameters)

	@property
	def bucket_task_board_format(self,
	) -> BucketTaskBoardFormatRequest:
		from .bucket_task_board_format import BucketTaskBoardFormatRequest
		return BucketTaskBoardFormatRequest(self.request_adapter, self.path_parameters)

	@property
	def details(self,
	) -> DetailsRequest:
		from .details import DetailsRequest
		return DetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def progress_task_board_format(self,
	) -> ProgressTaskBoardFormatRequest:
		from .progress_task_board_format import ProgressTaskBoardFormatRequest
		return ProgressTaskBoardFormatRequest(self.request_adapter, self.path_parameters)

