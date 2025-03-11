# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_room_list import GraphRoomListRequest
	from .graph_room import GraphRoomRequest
	from .count import CountRequest
	from .by_place_id import ByPlaceIdRequest
	from ...request_adapter import HttpxRequestAdapter


class PlacesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/places", path_parameters)

	def with_url(self, raw_url: str) -> PlacesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PlacesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PlacesRequest(self.request_adapter, self.path_parameters)

	def by_place_id(self,
		place_id: str,
	) -> ByPlaceIdRequest:
		if place_id is None:
			raise TypeError("place_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["place%2Did"] =  place_id

		from .by_place_id import ByPlaceIdRequest
		return ByPlaceIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_room(self,
	) -> GraphRoomRequest:
		from .graph_room import GraphRoomRequest
		return GraphRoomRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_room_list(self,
	) -> GraphRoomListRequest:
		from .graph_room_list import GraphRoomListRequest
		return GraphRoomListRequest(self.request_adapter, self.path_parameters)

