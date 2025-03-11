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
	from .participants import ParticipantsRequest
	from .operations import OperationsRequest
	from .update_recording_status import UpdateRecordingStatusRequest
	from .unmute import UnmuteRequest
	from .transfer import TransferRequest
	from .subscribe_to_tone import SubscribeToToneRequest
	from .stop_transcription import StopTranscriptionRequest
	from .stop_recording import StopRecordingRequest
	from .start_transcription import StartTranscriptionRequest
	from .start_recording import StartRecordingRequest
	from .send_dtmf_tones import SendDtmfTonesRequest
	from .reject import RejectRequest
	from .redirect import RedirectRequest
	from .record_response import RecordResponseRequest
	from .record import RecordRequest
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
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.call import Call


class ByCallIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/app/calls/{call%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Call:
		"""
		Get calls from app
		
		"""
		tags = ['app.call']

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
		Update the navigation property calls in app
		
		"""
		tags = ['app.call']

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
		Delete navigation property calls for app
		
		"""
		tags = ['app.call']
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

	def audio_routing_groups(self,
		call_id: str,
	) -> AudioRoutingGroupsRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .audio_routing_groups import AudioRoutingGroupsRequest
		return AudioRoutingGroupsRequest(self.request_adapter, path_parameters)

	def content_sharing_sessions(self,
		call_id: str,
	) -> ContentSharingSessionsRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .content_sharing_sessions import ContentSharingSessionsRequest
		return ContentSharingSessionsRequest(self.request_adapter, path_parameters)

	def add_large_gallery_view(self,
		call_id: str,
	) -> AddLargeGalleryViewRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .add_large_gallery_view import AddLargeGalleryViewRequest
		return AddLargeGalleryViewRequest(self.request_adapter, path_parameters)

	def answer(self,
		call_id: str,
	) -> AnswerRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .answer import AnswerRequest
		return AnswerRequest(self.request_adapter, path_parameters)

	def cancel_media_processing(self,
		call_id: str,
	) -> CancelMediaProcessingRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .cancel_media_processing import CancelMediaProcessingRequest
		return CancelMediaProcessingRequest(self.request_adapter, path_parameters)

	def change_screen_sharing_role(self,
		call_id: str,
	) -> ChangeScreenSharingRoleRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .change_screen_sharing_role import ChangeScreenSharingRoleRequest
		return ChangeScreenSharingRoleRequest(self.request_adapter, path_parameters)

	def keep_alive(self,
		call_id: str,
	) -> KeepAliveRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .keep_alive import KeepAliveRequest
		return KeepAliveRequest(self.request_adapter, path_parameters)

	def mute(self,
		call_id: str,
	) -> MuteRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .mute import MuteRequest
		return MuteRequest(self.request_adapter, path_parameters)

	def play_prompt(self,
		call_id: str,
	) -> PlayPromptRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .play_prompt import PlayPromptRequest
		return PlayPromptRequest(self.request_adapter, path_parameters)

	def record(self,
		call_id: str,
	) -> RecordRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .record import RecordRequest
		return RecordRequest(self.request_adapter, path_parameters)

	def record_response(self,
		call_id: str,
	) -> RecordResponseRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .record_response import RecordResponseRequest
		return RecordResponseRequest(self.request_adapter, path_parameters)

	def redirect(self,
		call_id: str,
	) -> RedirectRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .redirect import RedirectRequest
		return RedirectRequest(self.request_adapter, path_parameters)

	def reject(self,
		call_id: str,
	) -> RejectRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .reject import RejectRequest
		return RejectRequest(self.request_adapter, path_parameters)

	def send_dtmf_tones(self,
		call_id: str,
	) -> SendDtmfTonesRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .send_dtmf_tones import SendDtmfTonesRequest
		return SendDtmfTonesRequest(self.request_adapter, path_parameters)

	def start_recording(self,
		call_id: str,
	) -> StartRecordingRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .start_recording import StartRecordingRequest
		return StartRecordingRequest(self.request_adapter, path_parameters)

	def start_transcription(self,
		call_id: str,
	) -> StartTranscriptionRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .start_transcription import StartTranscriptionRequest
		return StartTranscriptionRequest(self.request_adapter, path_parameters)

	def stop_recording(self,
		call_id: str,
	) -> StopRecordingRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .stop_recording import StopRecordingRequest
		return StopRecordingRequest(self.request_adapter, path_parameters)

	def stop_transcription(self,
		call_id: str,
	) -> StopTranscriptionRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .stop_transcription import StopTranscriptionRequest
		return StopTranscriptionRequest(self.request_adapter, path_parameters)

	def subscribe_to_tone(self,
		call_id: str,
	) -> SubscribeToToneRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .subscribe_to_tone import SubscribeToToneRequest
		return SubscribeToToneRequest(self.request_adapter, path_parameters)

	def transfer(self,
		call_id: str,
	) -> TransferRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .transfer import TransferRequest
		return TransferRequest(self.request_adapter, path_parameters)

	def unmute(self,
		call_id: str,
	) -> UnmuteRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .unmute import UnmuteRequest
		return UnmuteRequest(self.request_adapter, path_parameters)

	def update_recording_status(self,
		call_id: str,
	) -> UpdateRecordingStatusRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .update_recording_status import UpdateRecordingStatusRequest
		return UpdateRecordingStatusRequest(self.request_adapter, path_parameters)

	def operations(self,
		call_id: str,
	) -> OperationsRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def participants(self,
		call_id: str,
	) -> ParticipantsRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .participants import ParticipantsRequest
		return ParticipantsRequest(self.request_adapter, path_parameters)

