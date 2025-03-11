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
	from .teams_app_definition import TeamsAppDefinitionRequest
	from .teams_app import TeamsAppRequest
	from .upgrade import UpgradeRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.teams_app_installation import TeamsAppInstallation


class ByTeamsAppInstallationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/chats/{chat%2Did}/installedApps/{teamsAppInstallation%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamsAppInstallation:
		"""
		Get installedApps from users
		A collection of all the apps in the chat. Nullable.
		"""
		tags = ['users.chat']

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
		return await self.request_adapter.send_async(request_info, TeamsAppInstallation, error_mapping)

	async def patch(
		self,
		body: TeamsAppInstallation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamsAppInstallation:
		"""
		Update the navigation property installedApps in users
		
		"""
		tags = ['users.chat']

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
		return await self.request_adapter.send_async(request_info, TeamsAppInstallation, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property installedApps for users
		
		"""
		tags = ['users.chat']
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



	def with_url(self, raw_url: str) -> ByTeamsAppInstallationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTeamsAppInstallationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTeamsAppInstallationIdRequest(self.request_adapter, self.path_parameters)

	def upgrade(self,
		user_id: str,
		chat_id: str,
		teamsAppInstallation_id: str,
	) -> UpgradeRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if teamsAppInstallation_id is None:
			raise TypeError("teamsAppInstallation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["teamsAppInstallation%2Did"] =  teamsAppInstallation_id

		from .upgrade import UpgradeRequest
		return UpgradeRequest(self.request_adapter, path_parameters)

	def teams_app(self,
		user_id: str,
		chat_id: str,
		teamsAppInstallation_id: str,
	) -> TeamsAppRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if teamsAppInstallation_id is None:
			raise TypeError("teamsAppInstallation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["teamsAppInstallation%2Did"] =  teamsAppInstallation_id

		from .teams_app import TeamsAppRequest
		return TeamsAppRequest(self.request_adapter, path_parameters)

	def teams_app_definition(self,
		user_id: str,
		chat_id: str,
		teamsAppInstallation_id: str,
	) -> TeamsAppDefinitionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if teamsAppInstallation_id is None:
			raise TypeError("teamsAppInstallation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["teamsAppInstallation%2Did"] =  teamsAppInstallation_id

		from .teams_app_definition import TeamsAppDefinitionRequest
		return TeamsAppDefinitionRequest(self.request_adapter, path_parameters)

