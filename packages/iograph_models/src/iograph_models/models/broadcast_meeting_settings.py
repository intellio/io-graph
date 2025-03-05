from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BroadcastMeetingSettings(BaseModel):
	allowedAudience: Optional[BroadcastMeetingAudience] = Field(default=None,alias="allowedAudience",)
	captions: Optional[BroadcastMeetingCaptionSettings] = Field(default=None,alias="captions",)
	isAttendeeReportEnabled: Optional[bool] = Field(default=None,alias="isAttendeeReportEnabled",)
	isQuestionAndAnswerEnabled: Optional[bool] = Field(default=None,alias="isQuestionAndAnswerEnabled",)
	isRecordingEnabled: Optional[bool] = Field(default=None,alias="isRecordingEnabled",)
	isVideoOnDemandEnabled: Optional[bool] = Field(default=None,alias="isVideoOnDemandEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .broadcast_meeting_audience import BroadcastMeetingAudience
from .broadcast_meeting_caption_settings import BroadcastMeetingCaptionSettings

