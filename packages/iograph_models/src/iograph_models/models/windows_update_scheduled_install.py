from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateScheduledInstall(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	scheduledInstallDay: Optional[WeeklySchedule] = Field(default=None,alias="scheduledInstallDay",)
	scheduledInstallTime: Optional[str] = Field(default=None,alias="scheduledInstallTime",)

from .weekly_schedule import WeeklySchedule

