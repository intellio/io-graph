from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DateTimeTimeZone(BaseModel):
	dateTime: Optional[str] = Field(alias="dateTime",default=None,)
	timeZone: Optional[str] = Field(alias="timeZone",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


