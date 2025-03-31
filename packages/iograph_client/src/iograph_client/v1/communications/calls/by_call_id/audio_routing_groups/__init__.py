# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_audio_routing_group_id import ByAudioRoutingGroupIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.audio_routing_group_collection_response import AudioRoutingGroupCollectionResponse
from iograph_models.v1.audio_routing_group import AudioRoutingGroup


class AudioRoutingGroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/audioRoutingGroups", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AudioRoutingGroupCollectionResponse:
		"""
		List audioRoutingGroups
		Retrieve a list of audioRoutingGroup objects.
		Find more info here: https://learn.microsoft.com/graph/api/call-list-audioroutinggroups?view=graph-rest-1.0
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, AudioRoutingGroupCollectionResponse, error_mapping)

	async def post(
		self,
		body: AudioRoutingGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AudioRoutingGroup:
		"""
		Create audioRoutingGroup
		Create a new audioRoutingGroup.
		Find more info here: https://learn.microsoft.com/graph/api/call-post-audioroutinggroups?view=graph-rest-1.0
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, AudioRoutingGroup, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AudioRoutingGroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AudioRoutingGroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AudioRoutingGroupsRequest(self.request_adapter, self.path_parameters)

	def by_audio_routing_group_id(self,
		call_id: str,
		audioRoutingGroup_id: str,
	) -> ByAudioRoutingGroupIdRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if audioRoutingGroup_id is None:
			raise TypeError("audioRoutingGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["audioRoutingGroup%2Did"] =  audioRoutingGroup_id

		from .by_audio_routing_group_id import ByAudioRoutingGroupIdRequest
		return ByAudioRoutingGroupIdRequest(self.request_adapter, path_parameters)

	def count(self,
		call_id: str,
	) -> CountRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

