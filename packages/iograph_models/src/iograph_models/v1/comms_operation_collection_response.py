from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CommsOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AddLargeGalleryViewOperation, CancelMediaProcessingOperation, InviteParticipantsOperation, MuteParticipantOperation, PlayPromptOperation, RecordOperation, SendDtmfTonesOperation, StartHoldMusicOperation, StopHoldMusicOperation, SubscribeToToneOperation, UnmuteParticipantOperation, UpdateRecordingStatusOperation],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
from .cancel_media_processing_operation import CancelMediaProcessingOperation
from .invite_participants_operation import InviteParticipantsOperation
from .mute_participant_operation import MuteParticipantOperation
from .play_prompt_operation import PlayPromptOperation
from .record_operation import RecordOperation
from .send_dtmf_tones_operation import SendDtmfTonesOperation
from .start_hold_music_operation import StartHoldMusicOperation
from .stop_hold_music_operation import StopHoldMusicOperation
from .subscribe_to_tone_operation import SubscribeToToneOperation
from .unmute_participant_operation import UnmuteParticipantOperation
from .update_recording_status_operation import UpdateRecordingStatusOperation

