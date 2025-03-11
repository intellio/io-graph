from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkOnlineMeetingInfo(BaseModel):
	calendarEventId: Optional[str] = Field(alias="calendarEventId",default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl",default=None,)
	organizer: Optional[TeamworkUserIdentity] = Field(alias="organizer",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_user_identity import TeamworkUserIdentity

