from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettings(BaseModel):
	deviceComplianceCheckinThresholdDays: Optional[int] = Field(alias="deviceComplianceCheckinThresholdDays",default=None,)
	isScheduledActionEnabled: Optional[bool] = Field(alias="isScheduledActionEnabled",default=None,)
	secureByDefault: Optional[bool] = Field(alias="secureByDefault",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


