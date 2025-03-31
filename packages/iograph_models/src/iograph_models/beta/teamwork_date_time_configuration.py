from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkDateTimeConfiguration(BaseModel):
	dateFormat: Optional[str] = Field(alias="dateFormat", default=None,)
	officeHoursEndTime: Optional[str] = Field(alias="officeHoursEndTime", default=None,)
	officeHoursStartTime: Optional[str] = Field(alias="officeHoursStartTime", default=None,)
	timeFormat: Optional[str] = Field(alias="timeFormat", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

