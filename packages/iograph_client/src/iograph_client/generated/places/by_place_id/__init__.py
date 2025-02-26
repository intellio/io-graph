# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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


class ByPlaceIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/places/{place%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

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

