from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementComplianceScheduledActionForRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	ruleName: Optional[str] = Field(alias="ruleName", default=None,)
	scheduledActionConfigurations: Optional[list[DeviceManagementComplianceActionItem]] = Field(alias="scheduledActionConfigurations", default=None,)

from .device_management_compliance_action_item import DeviceManagementComplianceActionItem

