# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tasks import TasksRequest
	from .details import DetailsRequest
	from .buckets import BucketsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.planner_plan import PlannerPlan
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPlannerPlanIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/planner/plans/{plannerPlan%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerPlan:
		"""
		Get plans from users
		Read-only. Nullable. Returns the plannerTasks assigned to the user.
		"""
		tags = ['users.plannerUser']

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
		return await self.request_adapter.send_async(request_info, PlannerPlan, error_mapping)

	async def patch(
		self,
		body: PlannerPlan,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerPlan:
		"""
		Update the navigation property plans in users
		
		"""
		tags = ['users.plannerUser']

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
		return await self.request_adapter.send_async(request_info, PlannerPlan, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property plans for users
		
		"""
		tags = ['users.plannerUser']
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



	def with_url(self, raw_url: str) -> ByPlannerPlanIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPlannerPlanIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPlannerPlanIdRequest(self.request_adapter, self.path_parameters)

	def buckets(self,
		user_id: str,
		plannerPlan_id: str,
	) -> BucketsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id

		from .buckets import BucketsRequest
		return BucketsRequest(self.request_adapter, path_parameters)

	def details(self,
		user_id: str,
		plannerPlan_id: str,
	) -> DetailsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id

		from .details import DetailsRequest
		return DetailsRequest(self.request_adapter, path_parameters)

	def tasks(self,
		user_id: str,
		plannerPlan_id: str,
	) -> TasksRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if plannerPlan_id is None:
			raise TypeError("plannerPlan_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["plannerPlan%2Did"] =  plannerPlan_id

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

