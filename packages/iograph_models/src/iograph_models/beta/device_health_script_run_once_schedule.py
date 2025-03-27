from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptRunOnceSchedule(BaseModel):
	interval: Optional[int] = Field(alias="interval", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptRunOnceSchedule"] = Field(alias="@odata.type", default="#microsoft.graph.deviceHealthScriptRunOnceSchedule")
	time: Optional[str] = Field(alias="time", default=None,)
	useUtc: Optional[bool] = Field(alias="useUtc", default=None,)
	date: Optional[str] = Field(alias="date", default=None,)


