from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Create_or_getPostRequest(BaseModel):
	chatInfo: Optional[ChatInfo] = Field(default=None,alias="chatInfo",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	participants: Optional[MeetingParticipants] = Field(default=None,alias="participants",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	subject: Optional[str] = Field(default=None,alias="subject",)

from .chat_info import ChatInfo
from .meeting_participants import MeetingParticipants

