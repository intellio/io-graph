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
	from .rooms import RoomsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.room_list import RoomList
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class GraphRoomListRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/places/{place%2Did}/graph.roomList", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RoomList:
		"""
		Get the item of type microsoft.graph.place as microsoft.graph.roomList
		
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
		return await self.request_adapter.send_async(request_info, RoomList, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> GraphRoomListRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GraphRoomListRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GraphRoomListRequest(self.request_adapter, self.path_parameters)

	def rooms(self,
		place_id: str,
	) -> RoomsRequest:
		if place_id is None:
			raise TypeError("place_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["place%2Did"] =  place_id

		from .rooms import RoomsRequest
		return RoomsRequest(self.request_adapter, path_parameters)

