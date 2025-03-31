from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesScheduleSettings(BaseModel):
	gradualRollout: Optional[Union[WindowsUpdatesDateDrivenRolloutSettings, WindowsUpdatesDurationDrivenRolloutSettings, WindowsUpdatesRateDrivenRolloutSettings]] = Field(alias="gradualRollout", default=None,discriminator="odata_type", )
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_date_driven_rollout_settings import WindowsUpdatesDateDrivenRolloutSettings
from .windows_updates_duration_driven_rollout_settings import WindowsUpdatesDurationDrivenRolloutSettings
from .windows_updates_rate_driven_rollout_settings import WindowsUpdatesRateDrivenRolloutSettings
