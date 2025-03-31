from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IosUpdateDeviceStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosUpdateDeviceStatus"] = Field(alias="@odata.type",)
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(alias="complianceGracePeriodExpirationDateTime", default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	installStatus: Optional[IosUpdatesInstallStatus | str] = Field(alias="installStatus", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	status: Optional[ComplianceStatus | str] = Field(alias="status", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .ios_updates_install_status import IosUpdatesInstallStatus
from .compliance_status import ComplianceStatus
