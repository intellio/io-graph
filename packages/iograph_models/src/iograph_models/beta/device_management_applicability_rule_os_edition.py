from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementApplicabilityRuleOsEdition(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	osEditionTypes: Optional[list[Windows10EditionType | str]] = Field(alias="osEditionTypes",default=None,)
	ruleType: Optional[DeviceManagementApplicabilityRuleType | str] = Field(alias="ruleType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows10_edition_type import Windows10EditionType
from .device_management_applicability_rule_type import DeviceManagementApplicabilityRuleType

