from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class CommsOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.addLargeGalleryViewOperation":
				from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
				return AddLargeGalleryViewOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.cancelMediaProcessingOperation":
				from .cancel_media_processing_operation import CancelMediaProcessingOperation
				return CancelMediaProcessingOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.inviteParticipantsOperation":
				from .invite_participants_operation import InviteParticipantsOperation
				return InviteParticipantsOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.muteParticipantOperation":
				from .mute_participant_operation import MuteParticipantOperation
				return MuteParticipantOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.playPromptOperation":
				from .play_prompt_operation import PlayPromptOperation
				return PlayPromptOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.recordOperation":
				from .record_operation import RecordOperation
				return RecordOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.sendDtmfTonesOperation":
				from .send_dtmf_tones_operation import SendDtmfTonesOperation
				return SendDtmfTonesOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.startHoldMusicOperation":
				from .start_hold_music_operation import StartHoldMusicOperation
				return StartHoldMusicOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.stopHoldMusicOperation":
				from .stop_hold_music_operation import StopHoldMusicOperation
				return StopHoldMusicOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.subscribeToToneOperation":
				from .subscribe_to_tone_operation import SubscribeToToneOperation
				return SubscribeToToneOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.unmuteParticipantOperation":
				from .unmute_participant_operation import UnmuteParticipantOperation
				return UnmuteParticipantOperation.model_validate(data)
			if mapping_key == "#microsoft.graph.updateRecordingStatusOperation":
				from .update_recording_status_operation import UpdateRecordingStatusOperation
				return UpdateRecordingStatusOperation.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .result_info import ResultInfo
from .operation_status import OperationStatus

