from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementApplicabilityRuleDeviceMode(BaseModel):
	deviceMode: Optional[Windows10DeviceModeType | str] = Field(alias="deviceMode", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	ruleType: Optional[DeviceManagementApplicabilityRuleType | str] = Field(alias="ruleType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows10_device_mode_type import Windows10DeviceModeType
from .device_management_applicability_rule_type import DeviceManagementApplicabilityRuleType
