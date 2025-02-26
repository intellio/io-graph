# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_teams_tab_id import ByTeamsTabIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.teams_tab import TeamsTab
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.teams_tab_collection_response import TeamsTabCollectionResponse


class TabsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/chats/{chat%2Did}/tabs"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TeamsTabCollectionResponse:
		"""
		Get tabs from users
		A collection of all the tabs in the chat. Nullable.
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
		return await self.request_adapter.send_async(request_info, TeamsTabCollectionResponse, error_mapping)

	async def post(
		self,
		body: TeamsTab,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TeamsTab:
		"""
		Create new navigation property to tabs for users
		
		"""
		tags = ['users.chat']

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
		return await self.request_adapter.send_async(request_info, TeamsTab, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_teams_tab_id(self,
		user_id: str,
		chat_id: str,
		teamsTab_id: str,
	) -> ByTeamsTabIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if teamsTab_id is None:
			raise TypeError("teamsTab_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["teamsTab%2Did"] =  teamsTab_id

		from .by_teams_tab_id import ByTeamsTabIdRequest
		return ByTeamsTabIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

