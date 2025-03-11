from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesScheduleSettings(BaseModel):
	gradualRollout: SerializeAsAny[Optional[WindowsUpdatesGradualRolloutSettings]] = Field(alias="gradualRollout",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_updates_gradual_rollout_settings import WindowsUpdatesGradualRolloutSettings

