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
	from .teams_app_definition import TeamsAppDefinitionRequest
	from .teams_app import TeamsAppRequest
	from .chat import ChatRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.user_scope_teams_app_installation import UserScopeTeamsAppInstallation
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserScopeTeamsAppInstallationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/teamwork/installedApps/{userScopeTeamsAppInstallation%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserScopeTeamsAppInstallation:
		"""
		Get installed app for user
		Retrieve the app installed in the personal scope of the specified user.
		Find more info here: https://learn.microsoft.com/graph/api/userteamwork-get-installedapps?view=graph-rest-1.0
		"""
		tags = ['users.userTeamwork']

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
		return await self.request_adapter.send_async(request_info, UserScopeTeamsAppInstallation, error_mapping)

	async def patch(
		self,
		body: UserScopeTeamsAppInstallation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserScopeTeamsAppInstallation:
		"""
		Update the navigation property installedApps in users
		
		"""
		tags = ['users.userTeamwork']

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
		return await self.request_adapter.send_async(request_info, UserScopeTeamsAppInstallation, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Uninstall app for user
		Uninstall an app from the personal scope of the specified user.
		Find more info here: https://learn.microsoft.com/graph/api/userteamwork-delete-installedapps?view=graph-rest-1.0
		"""
		tags = ['users.userTeamwork']
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



	def with_url(self, raw_url: str) -> ByUserScopeTeamsAppInstallationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserScopeTeamsAppInstallationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserScopeTeamsAppInstallationIdRequest(self.request_adapter, self.path_parameters)

	def chat(self,
		user_id: str,
		userScopeTeamsAppInstallation_id: str,
	) -> ChatRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if userScopeTeamsAppInstallation_id is None:
			raise TypeError("userScopeTeamsAppInstallation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["userScopeTeamsAppInstallation%2Did"] =  userScopeTeamsAppInstallation_id

		from .chat import ChatRequest
		return ChatRequest(self.request_adapter, path_parameters)

	def teams_app(self,
		user_id: str,
		userScopeTeamsAppInstallation_id: str,
	) -> TeamsAppRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if userScopeTeamsAppInstallation_id is None:
			raise TypeError("userScopeTeamsAppInstallation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["userScopeTeamsAppInstallation%2Did"] =  userScopeTeamsAppInstallation_id

		from .teams_app import TeamsAppRequest
		return TeamsAppRequest(self.request_adapter, path_parameters)

	def teams_app_definition(self,
		user_id: str,
		userScopeTeamsAppInstallation_id: str,
	) -> TeamsAppDefinitionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if userScopeTeamsAppInstallation_id is None:
			raise TypeError("userScopeTeamsAppInstallation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["userScopeTeamsAppInstallation%2Did"] =  userScopeTeamsAppInstallation_id

		from .teams_app_definition import TeamsAppDefinitionRequest
		return TeamsAppDefinitionRequest(self.request_adapter, path_parameters)

