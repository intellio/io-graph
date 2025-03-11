# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .stop_hold_music import StopHoldMusicRequest
	from .start_hold_music import StartHoldMusicRequest
	from .mute import MuteRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.participant import Participant


class ByParticipantIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/participants/{participant%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Participant:
		"""
		Get participant
		Retrieve the properties and relationships of a participant object.
		Find more info here: https://learn.microsoft.com/graph/api/participant-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, Participant, error_mapping)

	async def patch(
		self,
		body: Participant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Participant:
		"""
		Update the navigation property participants in communications
		
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
		return await self.request_adapter.send_async(request_info, Participant, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete participant
		Delete a specific participant in a call. In some situations, it is appropriate for an application to remove a participant from an active call. This action can be done before or after the participant answers the call. When an active caller is removed, they are immediately dropped from the call with no pre- or post-removal notification. When an invited participant is removed, any outstanding add participant request is canceled. 
		Find more info here: https://learn.microsoft.com/graph/api/participant-delete?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByParticipantIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByParticipantIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByParticipantIdRequest(self.request_adapter, self.path_parameters)

	def mute(self,
		call_id: str,
		participant_id: str,
	) -> MuteRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if participant_id is None:
			raise TypeError("participant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["participant%2Did"] =  participant_id

		from .mute import MuteRequest
		return MuteRequest(self.request_adapter, path_parameters)

	def start_hold_music(self,
		call_id: str,
		participant_id: str,
	) -> StartHoldMusicRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if participant_id is None:
			raise TypeError("participant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["participant%2Did"] =  participant_id

		from .start_hold_music import StartHoldMusicRequest
		return StartHoldMusicRequest(self.request_adapter, path_parameters)

	def stop_hold_music(self,
		call_id: str,
		participant_id: str,
	) -> StopHoldMusicRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if participant_id is None:
			raise TypeError("participant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["participant%2Did"] =  participant_id

		from .stop_hold_music import StopHoldMusicRequest
		return StopHoldMusicRequest(self.request_adapter, path_parameters)

