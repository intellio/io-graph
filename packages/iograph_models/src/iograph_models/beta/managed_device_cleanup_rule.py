from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedDeviceCleanupRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedDeviceCleanupRule"] = Field(alias="@odata.type", default="#microsoft.graph.managedDeviceCleanupRule")
	description: Optional[str] = Field(alias="description", default=None,)
	deviceCleanupRulePlatformType: Optional[DeviceCleanupRulePlatformType | str] = Field(alias="deviceCleanupRulePlatformType", default=None,)
	deviceInactivityBeforeRetirementInDays: Optional[int] = Field(alias="deviceInactivityBeforeRetirementInDays", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)

from .device_cleanup_rule_platform_type import DeviceCleanupRulePlatformType
