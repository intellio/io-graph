# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .progress_task_board_format import ProgressTaskBoardFormatRequest
	from .details import DetailsRequest
	from .bucket_task_board_format import BucketTaskBoardFormatRequest
	from .assigned_to_task_board_format import AssignedToTaskBoardFormatRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.beta.planner_task import PlannerTask
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPlannerTaskIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamTemplateDefinition/{teamTemplateDefinition%2Did}/teamDefinition/channels/{channel%2Did}/planner/plans/{plannerPlan%2Did}/tasks/{plannerTask%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerTask:
		"""
		Get tasks from teamTemplateDefinition
		Collection of tasks in the plan. Read-only. Nullable.
		"""
		tags = ['teamTemplateDefinition.team']

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
		Update the navigation property tasks in teamTemplateDefinition
		
		"""
		tags = ['teamTemplateDefinition.team']

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
		Delete navigation property tasks for teamTemplateDefinition
		
		"""
		tags = ['teamTemplateDefinition.team']
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



	def with_url(self, raw_url: str) -> ByPlannerTaskIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPlannerTaskIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPlannerTaskIdRequest(self.request_adapter, self.path_parameters)

	def assigned_to_task_board_format(self,
		teamTemplateDefinition_id: str,
		channel_id: str,
		plannerPlan_id: str,
		plannerTask_id: str,
	) -> AssignedToTaskBoardFormatRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")
		if plannerTask_id is None:
			raise TypeError("plannerTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id
		path_parameters["plannerTask%2Did"] =  plannerTask_id

		from .assigned_to_task_board_format import AssignedToTaskBoardFormatRequest
		return AssignedToTaskBoardFormatRequest(self.request_adapter, path_parameters)

	def bucket_task_board_format(self,
		teamTemplateDefinition_id: str,
		channel_id: str,
		plannerPlan_id: str,
		plannerTask_id: str,
	) -> BucketTaskBoardFormatRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")
		if plannerTask_id is None:
			raise TypeError("plannerTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id
		path_parameters["plannerTask%2Did"] =  plannerTask_id

		from .bucket_task_board_format import BucketTaskBoardFormatRequest
		return BucketTaskBoardFormatRequest(self.request_adapter, path_parameters)

	def details(self,
		teamTemplateDefinition_id: str,
		channel_id: str,
		plannerPlan_id: str,
		plannerTask_id: str,
	) -> DetailsRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")
		if plannerTask_id is None:
			raise TypeError("plannerTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id
		path_parameters["plannerTask%2Did"] =  plannerTask_id

		from .details import DetailsRequest
		return DetailsRequest(self.request_adapter, path_parameters)

	def progress_task_board_format(self,
		teamTemplateDefinition_id: str,
		channel_id: str,
		plannerPlan_id: str,
		plannerTask_id: str,
	) -> ProgressTaskBoardFormatRequest:
		if teamTemplateDefinition_id is None:
			raise TypeError("teamTemplateDefinition_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")
		if plannerTask_id is None:
			raise TypeError("plannerTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamTemplateDefinition%2Did"] =  teamTemplateDefinition_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id
		path_parameters["plannerTask%2Did"] =  plannerTask_id

		from .progress_task_board_format import ProgressTaskBoardFormatRequest
		return ProgressTaskBoardFormatRequest(self.request_adapter, path_parameters)

