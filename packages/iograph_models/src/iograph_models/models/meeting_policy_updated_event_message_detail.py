from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingPolicyUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)
	meetingChatEnabled: Optional[bool] = Field(default=None,alias="meetingChatEnabled",)
	meetingChatId: Optional[str] = Field(default=None,alias="meetingChatId",)

from .identity_set import IdentitySet

