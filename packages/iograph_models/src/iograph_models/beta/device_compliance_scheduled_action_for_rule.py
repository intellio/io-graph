from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceComplianceScheduledActionForRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceComplianceScheduledActionForRule"] = Field(alias="@odata.type",)
	ruleName: Optional[str] = Field(alias="ruleName", default=None,)
	scheduledActionConfigurations: Optional[list[DeviceComplianceActionItem]] = Field(alias="scheduledActionConfigurations", default=None,)

from .device_compliance_action_item import DeviceComplianceActionItem
