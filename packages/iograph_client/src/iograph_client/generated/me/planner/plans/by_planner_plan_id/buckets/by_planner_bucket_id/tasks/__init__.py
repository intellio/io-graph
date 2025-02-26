# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_planner_task_id import ByPlannerTaskIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.planner_task_collection_response import PlannerTaskCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.planner_task import PlannerTask


class TasksRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/planner/plans/{plannerPlan%2Did}/buckets/{plannerBucket%2Did}/tasks"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerTaskCollectionResponse:
		"""
		Get tasks from me
		Read-only. Nullable. The collection of tasks in the bucket.
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
		return await self.request_adapter.send_async(request_info, PlannerTaskCollectionResponse, error_mapping)

	async def post(
		self,
		body: PlannerTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerTask:
		"""
		Create new navigation property to tasks for me
		
		"""
		tags = ['me.plannerUser']

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
		return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_planner_task_id(self,
		plannerPlan_id: str,
		plannerBucket_id: str,
		plannerTask_id: str,
	) -> ByPlannerTaskIdRequest:
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")
		if plannerBucket_id is None:
			raise TypeError("plannerBucket_id cannot be null.")
		if plannerTask_id is None:
			raise TypeError("plannerTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id
		path_parameters["plannerBucket%2Did"] =  plannerBucket_id
		path_parameters["plannerTask%2Did"] =  plannerTask_id

		from .by_planner_task_id import ByPlannerTaskIdRequest
		return ByPlannerTaskIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

