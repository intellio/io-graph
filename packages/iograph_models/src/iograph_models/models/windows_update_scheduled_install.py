from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateScheduledInstall(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	scheduledInstallDay: Optional[WeeklySchedule | str] = Field(alias="scheduledInstallDay",default=None,)
	scheduledInstallTime: Optional[str] = Field(alias="scheduledInstallTime",default=None,)

from .weekly_schedule import WeeklySchedule

