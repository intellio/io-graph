from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Create_or_getPostRequest(BaseModel):
	chatInfo: Optional[ChatInfo] = Field(alias="chatInfo", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	participants: Optional[MeetingParticipants] = Field(alias="participants", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)

from .chat_info import ChatInfo
from .meeting_participants import MeetingParticipants

