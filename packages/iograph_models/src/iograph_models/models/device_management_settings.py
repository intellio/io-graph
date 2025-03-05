from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettings(BaseModel):
	deviceComplianceCheckinThresholdDays: Optional[int] = Field(default=None,alias="deviceComplianceCheckinThresholdDays",)
	isScheduledActionEnabled: Optional[bool] = Field(default=None,alias="isScheduledActionEnabled",)
	secureByDefault: Optional[bool] = Field(default=None,alias="secureByDefault",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


