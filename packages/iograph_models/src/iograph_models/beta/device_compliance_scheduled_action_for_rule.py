from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScheduledActionForRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	ruleName: Optional[str] = Field(alias="ruleName", default=None,)
	scheduledActionConfigurations: Optional[list[DeviceComplianceActionItem]] = Field(alias="scheduledActionConfigurations", default=None,)

from .device_compliance_action_item import DeviceComplianceActionItem

