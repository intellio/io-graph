from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConfigManagerPolicySummary(BaseModel):
	compliantDeviceCount: Optional[int] = Field(alias="compliantDeviceCount", default=None,)
	enforcedDeviceCount: Optional[int] = Field(alias="enforcedDeviceCount", default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)
	nonCompliantDeviceCount: Optional[int] = Field(alias="nonCompliantDeviceCount", default=None,)
	pendingDeviceCount: Optional[int] = Field(alias="pendingDeviceCount", default=None,)
	targetedDeviceCount: Optional[int] = Field(alias="targetedDeviceCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

