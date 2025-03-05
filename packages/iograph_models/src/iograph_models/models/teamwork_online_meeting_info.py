from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkOnlineMeetingInfo(BaseModel):
	calendarEventId: Optional[str] = Field(default=None,alias="calendarEventId",)
	joinWebUrl: Optional[str] = Field(default=None,alias="joinWebUrl",)
	organizer: Optional[TeamworkUserIdentity] = Field(default=None,alias="organizer",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .teamwork_user_identity import TeamworkUserIdentity

