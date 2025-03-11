from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScheduledActionForRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(alias="value",default=None,)

from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

