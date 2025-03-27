# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_teams_app_id import ByTeamsAppIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.teams_app import TeamsApp
from iograph_models.v1.teams_app_collection_response import TeamsAppCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class TeamsAppsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/appCatalogs/teamsApps", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamsAppCollectionResponse:
		"""
		List teamsApp
		List apps from the Microsoft Teams app catalog, including apps from the Microsoft Teams store and apps from your organization's app catalog (the tenant app catalog). To get apps from your organization's app catalog only, specify organization as the distributionMethod in the request.
		Find more info here: https://learn.microsoft.com/graph/api/appcatalogs-list-teamsapps?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, TeamsAppCollectionResponse, error_mapping)

	async def post(
		self,
		body: TeamsApp,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamsApp:
		"""
		Publish teamsApp
		Publish an app to the Microsoft Teams app catalog.
Specifically, this API publishes the app to your organization's catalog (the tenant app catalog);
the created resource has a distributionMethod property value of organization. The requiresReview property allows any user to submit an app for review by an administrator. Admins can approve or reject these apps via this API or the Microsoft Teams admin center.
		Find more info here: https://learn.microsoft.com/graph/api/teamsapp-publish?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, TeamsApp, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TeamsAppsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TeamsAppsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TeamsAppsRequest(self.request_adapter, self.path_parameters)

	def by_teams_app_id(self,
		teamsApp_id: str,
	) -> ByTeamsAppIdRequest:
		if teamsApp_id is None:
			raise TypeError("teamsApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamsApp%2Did"] =  teamsApp_id

		from .by_teams_app_id import ByTeamsAppIdRequest
		return ByTeamsAppIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

