from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosUpdateDeviceStatus(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(default=None,alias="complianceGracePeriodExpirationDateTime",)
	deviceDisplayName: Optional[str] = Field(default=None,alias="deviceDisplayName",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceModel: Optional[str] = Field(default=None,alias="deviceModel",)
	installStatus: Optional[IosUpdatesInstallStatus] = Field(default=None,alias="installStatus",)
	lastReportedDateTime: Optional[datetime] = Field(default=None,alias="lastReportedDateTime",)
	osVersion: Optional[str] = Field(default=None,alias="osVersion",)
	status: Optional[ComplianceStatus] = Field(default=None,alias="status",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userName: Optional[str] = Field(default=None,alias="userName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .ios_updates_install_status import IosUpdatesInstallStatus
from .compliance_status import ComplianceStatus

