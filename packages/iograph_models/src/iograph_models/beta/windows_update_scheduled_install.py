from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateScheduledInstall(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUpdateScheduledInstall"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdateScheduledInstall")
	scheduledInstallDay: Optional[WeeklySchedule | str] = Field(alias="scheduledInstallDay", default=None,)
	scheduledInstallTime: Optional[str] = Field(alias="scheduledInstallTime", default=None,)

from .weekly_schedule import WeeklySchedule

