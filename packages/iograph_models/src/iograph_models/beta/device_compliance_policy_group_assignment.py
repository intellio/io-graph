from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicyGroupAssignment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	excludeGroup: Optional[bool] = Field(alias="excludeGroup",default=None,)
	targetGroupId: Optional[str] = Field(alias="targetGroupId",default=None,)
	deviceCompliancePolicy: SerializeAsAny[Optional[DeviceCompliancePolicy]] = Field(alias="deviceCompliancePolicy",default=None,)

from .device_compliance_policy import DeviceCompliancePolicy

