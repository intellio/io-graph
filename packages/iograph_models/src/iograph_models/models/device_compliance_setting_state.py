from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceSettingState(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(default=None,alias="complianceGracePeriodExpirationDateTime",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceModel: Optional[str] = Field(default=None,alias="deviceModel",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	setting: Optional[str] = Field(default=None,alias="setting",)
	settingName: Optional[str] = Field(default=None,alias="settingName",)
	state: Optional[ComplianceStatus] = Field(default=None,alias="state",)
	userEmail: Optional[str] = Field(default=None,alias="userEmail",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userName: Optional[str] = Field(default=None,alias="userName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)

from .compliance_status import ComplianceStatus

