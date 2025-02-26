# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .teams_app import TeamsAppRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.teams_tab import TeamsTab
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByTeamsTabIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/chats/{chat%2Did}/tabs/{teamsTab%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamsTab:
		"""
		Get tab in chat
		Retrieve the properties and relationships of the specified tab in a chat. 
		Find more info here: https://learn.microsoft.com/graph/api/chat-get-tabs?view=graph-rest-1.0
		"""
		tags = ['chats.teamsTab']

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
		return await self.request_adapter.send_async(request_info, TeamsTab, error_mapping)

	async def patch(
		self,
		body: TeamsTab,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamsTab:
		"""
		Update tab in chat
		Update the properties of the specified tab in a chat. 
This can be used to configure the content of the tab.
		Find more info here: https://learn.microsoft.com/graph/api/chat-patch-tabs?view=graph-rest-1.0
		"""
		tags = ['chats.teamsTab']

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
		return await self.request_adapter.send_async(request_info, TeamsTab, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete tab from chat
		Remove (unpin) a tab from the specified chat. 
		Find more info here: https://learn.microsoft.com/graph/api/chat-delete-tabs?view=graph-rest-1.0
		"""
		tags = ['chats.teamsTab']
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



	@property
	def teams_app(self,
	) -> TeamsAppRequest:
		from .teams_app import TeamsAppRequest
		return TeamsAppRequest(self.request_adapter, self.path_parameters)

