from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommsApplication(BaseModel):
	calls: Optional[list[Call]] = Field(alias="calls", default=None,)
	onlineMeetings: Optional[list[OnlineMeeting]] = Field(alias="onlineMeetings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .call import Call
from .online_meeting import OnlineMeeting
