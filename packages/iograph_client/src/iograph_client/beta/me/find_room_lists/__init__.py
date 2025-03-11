# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.find_room_lists_response import FindRoomListsResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class FindRoomListsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/findRoomLists()", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FindRoomListsResponse:
		"""
		Invoke function findRoomLists
		Get the room lists defined in a tenant, as represented by their emailAddress objects. Tenants can organize meeting rooms into room lists. In this API, each meeting room and room list is represented by an emailAddress instance.
You can get all the room lists in the tenant, get all the rooms in the tenant, or get all the rooms in a specific room list.
		Find more info here: https://learn.microsoft.com/graph/api/user-findroomlists?view=graph-rest-beta
		"""
		tags = ['me.user.Functions']

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
		return await self.request_adapter.send_async(request_info, FindRoomListsResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")

	def with_url(self, raw_url: str) -> FindRoomListsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FindRoomListsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FindRoomListsRequest(self.request_adapter, self.path_parameters)

