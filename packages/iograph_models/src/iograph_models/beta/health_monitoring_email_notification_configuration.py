from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HealthMonitoringEmailNotificationConfiguration(BaseModel):
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


