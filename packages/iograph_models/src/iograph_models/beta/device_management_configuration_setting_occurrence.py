from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementConfigurationSettingOccurrence(BaseModel):
	maxDeviceOccurrence: Optional[int] = Field(alias="maxDeviceOccurrence", default=None,)
	minDeviceOccurrence: Optional[int] = Field(alias="minDeviceOccurrence", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

