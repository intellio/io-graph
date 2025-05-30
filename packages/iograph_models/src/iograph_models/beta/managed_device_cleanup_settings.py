from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceCleanupSettings(BaseModel):
	deviceInactivityBeforeRetirementInDays: Optional[str] = Field(alias="deviceInactivityBeforeRetirementInDays", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

