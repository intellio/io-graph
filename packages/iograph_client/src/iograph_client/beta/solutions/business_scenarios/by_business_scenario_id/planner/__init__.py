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
	from .tasks import TasksRequest
	from .task_configuration import TaskConfigurationRequest
	from .plan_configuration import PlanConfigurationRequest
	from .get_plan import GetPlanRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.business_scenario_planner import BusinessScenarioPlanner


class PlannerRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/businessScenarios/{businessScenario%2Did}/planner", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BusinessScenarioPlanner:
		"""
		Get businessScenarioPlanner
		Read the properties and relationships of a businessScenarioPlanner object.
		Find more info here: https://learn.microsoft.com/graph/api/businessscenarioplanner-get?view=graph-rest-beta
		"""
		tags = ['solutions.businessScenario']

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
		return await self.request_adapter.send_async(request_info, BusinessScenarioPlanner, error_mapping)

	async def patch(
		self,
		body: BusinessScenarioPlanner,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BusinessScenarioPlanner:
		"""
		Update the navigation property planner in solutions
		
		"""
		tags = ['solutions.businessScenario']

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
		return await self.request_adapter.send_async(request_info, BusinessScenarioPlanner, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property planner for solutions
		
		"""
		tags = ['solutions.businessScenario']
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



	def with_url(self, raw_url: str) -> PlannerRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PlannerRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PlannerRequest(self.request_adapter, self.path_parameters)

	def get_plan(self,
		businessScenario_id: str,
	) -> GetPlanRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id

		from .get_plan import GetPlanRequest
		return GetPlanRequest(self.request_adapter, path_parameters)

	def plan_configuration(self,
		businessScenario_id: str,
	) -> PlanConfigurationRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id

		from .plan_configuration import PlanConfigurationRequest
		return PlanConfigurationRequest(self.request_adapter, path_parameters)

	def task_configuration(self,
		businessScenario_id: str,
	) -> TaskConfigurationRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id

		from .task_configuration import TaskConfigurationRequest
		return TaskConfigurationRequest(self.request_adapter, path_parameters)

	def tasks(self,
		businessScenario_id: str,
	) -> TasksRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

