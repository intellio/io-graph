# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .workforce_integrations import WorkforceIntegrationsRequest
	from .teams_app_settings import TeamsAppSettingsRequest
	from .send_activity_notification_to_recipients import SendActivityNotificationToRecipientsRequest
	from .deleted_teams import DeletedTeamsRequest
	from .deleted_chats import DeletedChatsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.teamwork import Teamwork
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class TeamworkRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teamwork", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Teamwork:
		"""
		Get teamwork
		Get the properties and relationships of a teamwork object, such as the region of the organization and whether Microsoft Teams is enabled.
		Find more info here: https://learn.microsoft.com/graph/api/teamwork-get?view=graph-rest-1.0
		"""
		tags = ['teamwork.teamwork']

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
		return await self.request_adapter.send_async(request_info, Teamwork, error_mapping)

	async def patch(
		self,
		body: Teamwork,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Teamwork:
		"""
		Update teamwork
		
		"""
		tags = ['teamwork.teamwork']

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
		return await self.request_adapter.send_async(request_info, Teamwork, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TeamworkRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TeamworkRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TeamworkRequest(self.request_adapter, self.path_parameters)

	@property
	def deleted_chats(self,
	) -> DeletedChatsRequest:
		from .deleted_chats import DeletedChatsRequest
		return DeletedChatsRequest(self.request_adapter, self.path_parameters)

	@property
	def deleted_teams(self,
	) -> DeletedTeamsRequest:
		from .deleted_teams import DeletedTeamsRequest
		return DeletedTeamsRequest(self.request_adapter, self.path_parameters)

	@property
	def send_activity_notification_to_recipients(self,
	) -> SendActivityNotificationToRecipientsRequest:
		from .send_activity_notification_to_recipients import SendActivityNotificationToRecipientsRequest
		return SendActivityNotificationToRecipientsRequest(self.request_adapter, self.path_parameters)

	@property
	def teams_app_settings(self,
	) -> TeamsAppSettingsRequest:
		from .teams_app_settings import TeamsAppSettingsRequest
		return TeamsAppSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def workforce_integrations(self,
	) -> WorkforceIntegrationsRequest:
		from .workforce_integrations import WorkforceIntegrationsRequest
		return WorkforceIntegrationsRequest(self.request_adapter, self.path_parameters)

