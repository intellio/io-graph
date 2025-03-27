from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RegionalFormatOverrides(BaseModel):
	calendar: Optional[str] = Field(alias="calendar", default=None,)
	firstDayOfWeek: Optional[str] = Field(alias="firstDayOfWeek", default=None,)
	longDateFormat: Optional[str] = Field(alias="longDateFormat", default=None,)
	longTimeFormat: Optional[str] = Field(alias="longTimeFormat", default=None,)
	shortDateFormat: Optional[str] = Field(alias="shortDateFormat", default=None,)
	shortTimeFormat: Optional[str] = Field(alias="shortTimeFormat", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


