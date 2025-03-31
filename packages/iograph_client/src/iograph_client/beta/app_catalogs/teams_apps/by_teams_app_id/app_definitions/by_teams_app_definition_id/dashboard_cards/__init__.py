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
	from .by_teams_app_dashboard_card_definition_id import ByTeamsAppDashboardCardDefinitionIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.teams_app_dashboard_card_definition import TeamsAppDashboardCardDefinition
from iograph_models.beta.teams_app_dashboard_card_definition_collection_response import TeamsAppDashboardCardDefinitionCollectionResponse


class DashboardCardsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/appCatalogs/teamsApps/{teamsApp%2Did}/appDefinitions/{teamsAppDefinition%2Did}/dashboardCards", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamsAppDashboardCardDefinitionCollectionResponse:
		"""
		Get dashboardCards from appCatalogs
		Dashboard cards specified in the Teams app manifest.
		"""
		tags = ['appCatalogs.teamsApp']

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
		return await self.request_adapter.send_async(request_info, TeamsAppDashboardCardDefinitionCollectionResponse, error_mapping)

	async def post(
		self,
		body: TeamsAppDashboardCardDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamsAppDashboardCardDefinition:
		"""
		Create new navigation property to dashboardCards for appCatalogs
		
		"""
		tags = ['appCatalogs.teamsApp']

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
		return await self.request_adapter.send_async(request_info, TeamsAppDashboardCardDefinition, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DashboardCardsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DashboardCardsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DashboardCardsRequest(self.request_adapter, self.path_parameters)

	def by_teams_app_dashboard_card_definition_id(self,
		teamsApp_id: str,
		teamsAppDefinition_id: str,
		teamsAppDashboardCardDefinition_id: str,
	) -> ByTeamsAppDashboardCardDefinitionIdRequest:
		if teamsApp_id is None:
			raise TypeError("teamsApp_id cannot be null.")
		if teamsAppDefinition_id is None:
			raise TypeError("teamsAppDefinition_id cannot be null.")
		if teamsAppDashboardCardDefinition_id is None:
			raise TypeError("teamsAppDashboardCardDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamsApp%2Did"] =  teamsApp_id
		path_parameters["teamsAppDefinition%2Did"] =  teamsAppDefinition_id
		path_parameters["teamsAppDashboardCardDefinition%2Did"] =  teamsAppDashboardCardDefinition_id

		from .by_teams_app_dashboard_card_definition_id import ByTeamsAppDashboardCardDefinitionIdRequest
		return ByTeamsAppDashboardCardDefinitionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		teamsApp_id: str,
		teamsAppDefinition_id: str,
	) -> CountRequest:
		if teamsApp_id is None:
			raise TypeError("teamsApp_id cannot be null.")
		if teamsAppDefinition_id is None:
			raise TypeError("teamsAppDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamsApp%2Did"] =  teamsApp_id
		path_parameters["teamsAppDefinition%2Did"] =  teamsAppDefinition_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

