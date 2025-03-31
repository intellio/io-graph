from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceHealthScriptHourlySchedule(BaseModel):
	interval: Optional[int] = Field(alias="interval", default=None,)
	odata_type: Literal["#microsoft.graph.deviceHealthScriptHourlySchedule"] = Field(alias="@odata.type", default="#microsoft.graph.deviceHealthScriptHourlySchedule")

