from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Validate_compliance_scriptPostRequest(BaseModel):
	deviceCompliancePolicyScript: Optional[DeviceCompliancePolicyScript] = Field(alias="deviceCompliancePolicyScript", default=None,)

from .device_compliance_policy_script import DeviceCompliancePolicyScript
