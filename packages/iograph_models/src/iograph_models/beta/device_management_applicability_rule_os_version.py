from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementApplicabilityRuleOsVersion(BaseModel):
	maxOSVersion: Optional[str] = Field(alias="maxOSVersion",default=None,)
	minOSVersion: Optional[str] = Field(alias="minOSVersion",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	ruleType: Optional[DeviceManagementApplicabilityRuleType | str] = Field(alias="ruleType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_applicability_rule_type import DeviceManagementApplicabilityRuleType

