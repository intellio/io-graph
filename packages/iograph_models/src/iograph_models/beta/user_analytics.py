from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserAnalytics(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	settings: Optional[Settings] = Field(alias="settings",default=None,)
	activityStatistics: SerializeAsAny[Optional[list[ActivityStatistics]]] = Field(alias="activityStatistics",default=None,)

from .settings import Settings
from .activity_statistics import ActivityStatistics

