from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityBaselineDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityBaselineDeviceState"] = Field(alias="@odata.type",)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	state: Optional[SecurityBaselineComplianceState | str] = Field(alias="state", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .security_baseline_compliance_state import SecurityBaselineComplianceState
