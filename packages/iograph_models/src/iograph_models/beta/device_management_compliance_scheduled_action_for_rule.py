from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementComplianceScheduledActionForRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementComplianceScheduledActionForRule"] = Field(alias="@odata.type",)
	ruleName: Optional[str] = Field(alias="ruleName", default=None,)
	scheduledActionConfigurations: Optional[list[DeviceManagementComplianceActionItem]] = Field(alias="scheduledActionConfigurations", default=None,)

from .device_management_compliance_action_item import DeviceManagementComplianceActionItem
