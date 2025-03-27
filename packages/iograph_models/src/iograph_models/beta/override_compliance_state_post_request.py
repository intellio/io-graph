from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Override_compliance_statePostRequest(BaseModel):
	complianceState: Optional[AdministratorConfiguredDeviceComplianceState | str] = Field(alias="complianceState", default=None,)
	remediationUrl: Optional[str] = Field(alias="remediationUrl", default=None,)

from .administrator_configured_device_compliance_state import AdministratorConfiguredDeviceComplianceState

