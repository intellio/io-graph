from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptDailySchedule(BaseModel):
	interval: Optional[int] = Field(alias="interval",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	time: Optional[str] = Field(alias="time",default=None,)
	useUtc: Optional[bool] = Field(alias="useUtc",default=None,)


