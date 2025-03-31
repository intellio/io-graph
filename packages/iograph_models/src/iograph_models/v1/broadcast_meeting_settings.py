from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BroadcastMeetingSettings(BaseModel):
	allowedAudience: Optional[BroadcastMeetingAudience | str] = Field(alias="allowedAudience", default=None,)
	captions: Optional[BroadcastMeetingCaptionSettings] = Field(alias="captions", default=None,)
	isAttendeeReportEnabled: Optional[bool] = Field(alias="isAttendeeReportEnabled", default=None,)
	isQuestionAndAnswerEnabled: Optional[bool] = Field(alias="isQuestionAndAnswerEnabled", default=None,)
	isRecordingEnabled: Optional[bool] = Field(alias="isRecordingEnabled", default=None,)
	isVideoOnDemandEnabled: Optional[bool] = Field(alias="isVideoOnDemandEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .broadcast_meeting_audience import BroadcastMeetingAudience
from .broadcast_meeting_caption_settings import BroadcastMeetingCaptionSettings
