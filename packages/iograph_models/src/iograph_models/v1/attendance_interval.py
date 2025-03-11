from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AttendanceInterval(BaseModel):
	durationInSeconds: Optional[int] = Field(alias="durationInSeconds",default=None,)
	joinDateTime: Optional[datetime] = Field(alias="joinDateTime",default=None,)
	leaveDateTime: Optional[datetime] = Field(alias="leaveDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


