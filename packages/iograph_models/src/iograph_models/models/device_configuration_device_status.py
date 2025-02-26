from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceConfigurationDeviceStatus(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(default=None,alias="complianceGracePeriodExpirationDateTime",)
	deviceDisplayName: Optional[str] = Field(default=None,alias="deviceDisplayName",)
	deviceModel: Optional[str] = Field(default=None,alias="deviceModel",)
	lastReportedDateTime: Optional[datetime] = Field(default=None,alias="lastReportedDateTime",)
	status: Optional[ComplianceStatus] = Field(default=None,alias="status",)
	userName: Optional[str] = Field(default=None,alias="userName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .compliance_status import ComplianceStatus

