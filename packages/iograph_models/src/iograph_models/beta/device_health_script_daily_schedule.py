from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceHealthScriptDailySchedule(BaseModel):
	interval: Optional[int] = Field(alias="interval", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptDailySchedule"] = Field(alias="@odata.type", default="#microsoft.graph.deviceHealthScriptDailySchedule")
	time: Optional[str] = Field(alias="time", default=None,)
	useUtc: Optional[bool] = Field(alias="useUtc", default=None,)

