from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class JoinMeetingIdSettings(BaseModel):
	isPasscodeRequired: Optional[bool] = Field(default=None,alias="isPasscodeRequired",)
	joinMeetingId: Optional[str] = Field(default=None,alias="joinMeetingId",)
	passcode: Optional[str] = Field(default=None,alias="passcode",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


