from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceComplianceScheduledActionForRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	ruleName: Optional[str] = Field(default=None,alias="ruleName",)
	scheduledActionConfigurations: list[DeviceComplianceActionItem] = Field(alias="scheduledActionConfigurations",)

from .device_compliance_action_item import DeviceComplianceActionItem

