from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceUserStatus(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	devicesCount: Optional[int] = Field(default=None,alias="devicesCount",)
	lastReportedDateTime: Optional[datetime] = Field(default=None,alias="lastReportedDateTime",)
	status: Optional[ComplianceStatus] = Field(default=None,alias="status",)
	userDisplayName: Optional[str] = Field(default=None,alias="userDisplayName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .compliance_status import ComplianceStatus

