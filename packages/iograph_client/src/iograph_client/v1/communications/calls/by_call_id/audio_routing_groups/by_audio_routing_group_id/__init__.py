# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.audio_routing_group import AudioRoutingGroup
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByAudioRoutingGroupIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/audioRoutingGroups/{audioRoutingGroup%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AudioRoutingGroup:
		"""
		Get audioRoutingGroup
		Retrieve the properties and relationships of an audioRoutingGroup object.
		Find more info here: https://learn.microsoft.com/graph/api/audioroutinggroup-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, AudioRoutingGroup, error_mapping)

	async def patch(
		self,
		body: AudioRoutingGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AudioRoutingGroup:
		"""
		Update audioRoutingGroup
		Modify sources and receivers of an audioRoutingGroup.
		Find more info here: https://learn.microsoft.com/graph/api/audioroutinggroup-update?view=graph-rest-1.0
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, AudioRoutingGroup, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete audioRoutingGroup
		Delete the specified audioRoutingGroup.
		Find more info here: https://learn.microsoft.com/graph/api/audioroutinggroup-delete?view=graph-rest-1.0
		"""
		tags = ['communications.call']
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



	def with_url(self, raw_url: str) -> ByAudioRoutingGroupIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAudioRoutingGroupIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAudioRoutingGroupIdRequest(self.request_adapter, self.path_parameters)

