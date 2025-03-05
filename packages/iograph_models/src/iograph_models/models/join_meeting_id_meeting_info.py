from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class JoinMeetingIdMeetingInfo(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	joinMeetingId: Optional[str] = Field(default=None,alias="joinMeetingId",)
	passcode: Optional[str] = Field(default=None,alias="passcode",)


