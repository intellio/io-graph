# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.room import Room
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class GraphRoomRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/places/{place%2Did}/graph.room", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Room:
		"""
		List places
		Get a collection of the specified type of place objects defined in the tenant. For example, you can get all the rooms, all the room lists, or the rooms in a specific room list in the tenant. A place object can be one of the following types: Both room and roomList are derived from the place object. By default, this operation returns 100 places per page. Compared with the findRooms and findRoomLists functions, this operation returns a richer payload for rooms and room lists. See details for how they compare.
		Find more info here: https://learn.microsoft.com/graph/api/place-list?view=graph-rest-1.0
		"""
		tags = ['places.place']

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
		return await self.request_adapter.send_async(request_info, Room, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> GraphRoomRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GraphRoomRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GraphRoomRequest(self.request_adapter, self.path_parameters)

