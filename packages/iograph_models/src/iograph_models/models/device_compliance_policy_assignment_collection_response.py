from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceCompliancePolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DeviceCompliancePolicyAssignment] = Field(alias="value",)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment

