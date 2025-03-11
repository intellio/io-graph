from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingPolicyUpdatedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	meetingChatEnabled: Optional[bool] = Field(alias="meetingChatEnabled",default=None,)
	meetingChatId: Optional[str] = Field(alias="meetingChatId",default=None,)

from .identity_set import IdentitySet

