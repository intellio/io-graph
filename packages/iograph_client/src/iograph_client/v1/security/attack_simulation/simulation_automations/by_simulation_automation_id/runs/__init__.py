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
	from .count import CountRequest
	from .by_simulation_automation_run_id import BySimulationAutomationRunIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.simulation_automation_run_collection_response import SimulationAutomationRunCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.simulation_automation_run import SimulationAutomationRun


class RunsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/attackSimulation/simulationAutomations/{simulationAutomation%2Did}/runs", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SimulationAutomationRunCollectionResponse:
		"""
		List runs
		Get a list of the attack simulation automation runs for a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/simulationautomation-list-runs?view=graph-rest-1.0
		"""
		tags = ['security.attackSimulationRoot']

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
		return await self.request_adapter.send_async(request_info, SimulationAutomationRunCollectionResponse, error_mapping)

	async def post(
		self,
		body: SimulationAutomationRun,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SimulationAutomationRun:
		"""
		Create new navigation property to runs for security
		
		"""
		tags = ['security.attackSimulationRoot']

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
		return await self.request_adapter.send_async(request_info, SimulationAutomationRun, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RunsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RunsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RunsRequest(self.request_adapter, self.path_parameters)

	def by_simulation_automation_run_id(self,
		simulationAutomation_id: str,
		simulationAutomationRun_id: str,
	) -> BySimulationAutomationRunIdRequest:
		if simulationAutomation_id is None:
			raise TypeError("simulationAutomation_id cannot be null.")
		if simulationAutomationRun_id is None:
			raise TypeError("simulationAutomationRun_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["simulationAutomation%2Did"] =  simulationAutomation_id
		path_parameters["simulationAutomationRun%2Did"] =  simulationAutomationRun_id

		from .by_simulation_automation_run_id import BySimulationAutomationRunIdRequest
		return BySimulationAutomationRunIdRequest(self.request_adapter, path_parameters)

	def count(self,
		simulationAutomation_id: str,
	) -> CountRequest:
		if simulationAutomation_id is None:
			raise TypeError("simulationAutomation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["simulationAutomation%2Did"] =  simulationAutomation_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

