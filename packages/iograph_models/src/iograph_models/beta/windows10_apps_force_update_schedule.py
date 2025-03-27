from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10AppsForceUpdateSchedule(BaseModel):
	recurrence: Optional[Windows10AppsUpdateRecurrence | str] = Field(alias="recurrence", default=None,)
	runImmediatelyIfAfterStartDateTime: Optional[bool] = Field(alias="runImmediatelyIfAfterStartDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows10_apps_update_recurrence import Windows10AppsUpdateRecurrence

