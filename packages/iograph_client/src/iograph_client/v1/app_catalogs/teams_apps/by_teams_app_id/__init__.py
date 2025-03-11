# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .app_definitions import AppDefinitionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.teams_app import TeamsApp


class ByTeamsAppIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/appCatalogs/teamsApps/{teamsApp%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamsApp:
		"""
		Get teamsApps from appCatalogs
		
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
		return await self.request_adapter.send_async(request_info, TeamsApp, error_mapping)

	async def patch(
		self,
		body: TeamsApp,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamsApp:
		"""
		Update the navigation property teamsApps in appCatalogs
		
		"""
		tags = ['appCatalogs.teamsApp']

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
		return await self.request_adapter.send_async(request_info, TeamsApp, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete teamsApp
		Delete an app from an organization's app catalog (the tenant app catalog). To delete an app, the distributionMethod property for the app must be set to organization. You can also use this API to remove a submitted app from the review process.
		Find more info here: https://learn.microsoft.com/graph/api/teamsapp-delete?view=graph-rest-1.0
		"""
		tags = ['appCatalogs.teamsApp']
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



	def with_url(self, raw_url: str) -> ByTeamsAppIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTeamsAppIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTeamsAppIdRequest(self.request_adapter, self.path_parameters)

	def app_definitions(self,
		teamsApp_id: str,
	) -> AppDefinitionsRequest:
		if teamsApp_id is None:
			raise TypeError("teamsApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["teamsApp%2Did"] =  teamsApp_id

		from .app_definitions import AppDefinitionsRequest
		return AppDefinitionsRequest(self.request_adapter, path_parameters)

