# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_room_list import GraphRoomListRequest
	from .graph_room import GraphRoomRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.place import Place
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPlaceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/places/{place%2Did}", path_parameters)

	async def patch(
		self,
		body: Place,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Place:
		"""
		Update place
		Update the properties of place object, which can be a room or roomList. You can identify the room or roomList by specifying the id or emailAddress property.
		Find more info here: https://learn.microsoft.com/graph/api/place-update?view=graph-rest-1.0
		"""
		tags = ['places.place']

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
		return await self.request_adapter.send_async(request_info, Place, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from places
		
		"""
		tags = ['places.place']
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



	def with_url(self, raw_url: str) -> ByPlaceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPlaceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPlaceIdRequest(self.request_adapter, self.path_parameters)

	def graph_room(self,
		place_id: str,
	) -> GraphRoomRequest:
		if place_id is None:
			raise TypeError("place_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["place%2Did"] =  place_id

		from .graph_room import GraphRoomRequest
		return GraphRoomRequest(self.request_adapter, path_parameters)

	def graph_room_list(self,
		place_id: str,
	) -> GraphRoomListRequest:
		if place_id is None:
			raise TypeError("place_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["place%2Did"] =  place_id

		from .graph_room_list import GraphRoomListRequest
		return GraphRoomListRequest(self.request_adapter, path_parameters)

