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
	from .participants import ParticipantsRequest
	from .operations import OperationsRequest
	from .update_recording_status import UpdateRecordingStatusRequest
	from .unmute import UnmuteRequest
	from .transfer import TransferRequest
	from .subscribe_to_tone import SubscribeToToneRequest
	from .send_dtmf_tones import SendDtmfTonesRequest
	from .reject import RejectRequest
	from .redirect import RedirectRequest
	from .record_response import RecordResponseRequest
	from .play_prompt import PlayPromptRequest
	from .mute import MuteRequest
	from .keep_alive import KeepAliveRequest
	from .change_screen_sharing_role import ChangeScreenSharingRoleRequest
	from .cancel_media_processing import CancelMediaProcessingRequest
	from .answer import AnswerRequest
	from .add_large_gallery_view import AddLargeGalleryViewRequest
	from .content_sharing_sessions import ContentSharingSessionsRequest
	from .audio_routing_groups import AudioRoutingGroupsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.call import Call
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByCallIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Call:
		"""
		Get call
		Retrieve the properties and relationships of a call object.
		Find more info here: https://learn.microsoft.com/graph/api/call-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, Call, error_mapping)

	async def patch(
		self,
		body: Call,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Call:
		"""
		Update the navigation property calls in communications
		
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
		return await self.request_adapter.send_async(request_info, Call, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete call
		Delete or hang up an active call. For group calls, this will only delete your call leg and the underlying group call will still continue.
		Find more info here: https://learn.microsoft.com/graph/api/call-delete?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByCallIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCallIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCallIdRequest(self.request_adapter, self.path_parameters)

	@property
	def audio_routing_groups(self,
	) -> AudioRoutingGroupsRequest:
		from .audio_routing_groups import AudioRoutingGroupsRequest
		return AudioRoutingGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def content_sharing_sessions(self,
	) -> ContentSharingSessionsRequest:
		from .content_sharing_sessions import ContentSharingSessionsRequest
		return ContentSharingSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def add_large_gallery_view(self,
	) -> AddLargeGalleryViewRequest:
		from .add_large_gallery_view import AddLargeGalleryViewRequest
		return AddLargeGalleryViewRequest(self.request_adapter, self.path_parameters)

	@property
	def answer(self,
	) -> AnswerRequest:
		from .answer import AnswerRequest
		return AnswerRequest(self.request_adapter, self.path_parameters)

	@property
	def cancel_media_processing(self,
	) -> CancelMediaProcessingRequest:
		from .cancel_media_processing import CancelMediaProcessingRequest
		return CancelMediaProcessingRequest(self.request_adapter, self.path_parameters)

	@property
	def change_screen_sharing_role(self,
	) -> ChangeScreenSharingRoleRequest:
		from .change_screen_sharing_role import ChangeScreenSharingRoleRequest
		return ChangeScreenSharingRoleRequest(self.request_adapter, self.path_parameters)

	@property
	def keep_alive(self,
	) -> KeepAliveRequest:
		from .keep_alive import KeepAliveRequest
		return KeepAliveRequest(self.request_adapter, self.path_parameters)

	@property
	def mute(self,
	) -> MuteRequest:
		from .mute import MuteRequest
		return MuteRequest(self.request_adapter, self.path_parameters)

	@property
	def play_prompt(self,
	) -> PlayPromptRequest:
		from .play_prompt import PlayPromptRequest
		return PlayPromptRequest(self.request_adapter, self.path_parameters)

	@property
	def record_response(self,
	) -> RecordResponseRequest:
		from .record_response import RecordResponseRequest
		return RecordResponseRequest(self.request_adapter, self.path_parameters)

	@property
	def redirect(self,
	) -> RedirectRequest:
		from .redirect import RedirectRequest
		return RedirectRequest(self.request_adapter, self.path_parameters)

	@property
	def reject(self,
	) -> RejectRequest:
		from .reject import RejectRequest
		return RejectRequest(self.request_adapter, self.path_parameters)

	@property
	def send_dtmf_tones(self,
	) -> SendDtmfTonesRequest:
		from .send_dtmf_tones import SendDtmfTonesRequest
		return SendDtmfTonesRequest(self.request_adapter, self.path_parameters)

	@property
	def subscribe_to_tone(self,
	) -> SubscribeToToneRequest:
		from .subscribe_to_tone import SubscribeToToneRequest
		return SubscribeToToneRequest(self.request_adapter, self.path_parameters)

	@property
	def transfer(self,
	) -> TransferRequest:
		from .transfer import TransferRequest
		return TransferRequest(self.request_adapter, self.path_parameters)

	@property
	def unmute(self,
	) -> UnmuteRequest:
		from .unmute import UnmuteRequest
		return UnmuteRequest(self.request_adapter, self.path_parameters)

	@property
	def update_recording_status(self,
	) -> UpdateRecordingStatusRequest:
		from .update_recording_status import UpdateRecordingStatusRequest
		return UpdateRecordingStatusRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def participants(self,
	) -> ParticipantsRequest:
		from .participants import ParticipantsRequest
		return ParticipantsRequest(self.request_adapter, self.path_parameters)

