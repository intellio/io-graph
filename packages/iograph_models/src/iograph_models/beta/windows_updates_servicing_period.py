from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesServicingPeriod(BaseModel):
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

