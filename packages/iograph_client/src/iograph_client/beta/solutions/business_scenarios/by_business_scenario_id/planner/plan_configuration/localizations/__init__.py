# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_planner_plan_configuration_localization_id import ByPlannerPlanConfigurationLocalizationIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.planner_plan_configuration_localization_collection_response import PlannerPlanConfigurationLocalizationCollectionResponse
from iograph_models.beta.planner_plan_configuration_localization import PlannerPlanConfigurationLocalization


class LocalizationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/businessScenarios/{businessScenario%2Did}/planner/planConfiguration/localizations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PlannerPlanConfigurationLocalizationCollectionResponse:
		"""
		List plannerPlanConfigurationLocalizations
		Get a list of the plannerPlanConfigurationLocalization objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/plannerplanconfiguration-list-localizations?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, PlannerPlanConfigurationLocalizationCollectionResponse, error_mapping)

	async def post(
		self,
		body: PlannerPlanConfigurationLocalization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PlannerPlanConfigurationLocalization:
		"""
		Create new navigation property to localizations for solutions
		
		"""
		tags = ['solutions.businessScenario']

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
		return await self.request_adapter.send_async(request_info, PlannerPlanConfigurationLocalization, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LocalizationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LocalizationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LocalizationsRequest(self.request_adapter, self.path_parameters)

	def by_planner_plan_configuration_localization_id(self,
		businessScenario_id: str,
		plannerPlanConfigurationLocalization_id: str,
	) -> ByPlannerPlanConfigurationLocalizationIdRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")
		if plannerPlanConfigurationLocalization_id is None:
			raise TypeError("plannerPlanConfigurationLocalization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id
		path_parameters["plannerPlanConfigurationLocalization%2Did"] =  plannerPlanConfigurationLocalization_id

		from .by_planner_plan_configuration_localization_id import ByPlannerPlanConfigurationLocalizationIdRequest
		return ByPlannerPlanConfigurationLocalizationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		businessScenario_id: str,
	) -> CountRequest:
		if businessScenario_id is None:
			raise TypeError("businessScenario_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["businessScenario%2Did"] =  businessScenario_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

