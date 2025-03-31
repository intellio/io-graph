from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class JoinMeetingIdSettings(BaseModel):
	isPasscodeRequired: Optional[bool] = Field(alias="isPasscodeRequired", default=None,)
	joinMeetingId: Optional[str] = Field(alias="joinMeetingId", default=None,)
	passcode: Optional[str] = Field(alias="passcode", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

