from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceComplianceUserStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceComplianceUserStatus"] = Field(alias="@odata.type", default="#microsoft.graph.deviceComplianceUserStatus")
	devicesCount: Optional[int] = Field(alias="devicesCount", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	status: Optional[ComplianceStatus | str] = Field(alias="status", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .compliance_status import ComplianceStatus
