from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceComplianceScheduledActionForRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(default=None,alias="value",)

from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

