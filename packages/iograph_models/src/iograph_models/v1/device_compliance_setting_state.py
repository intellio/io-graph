from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceComplianceSettingState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceComplianceSettingState"] = Field(alias="@odata.type", default="#microsoft.graph.deviceComplianceSettingState")
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(alias="complianceGracePeriodExpirationDateTime", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	setting: Optional[str] = Field(alias="setting", default=None,)
	settingName: Optional[str] = Field(alias="settingName", default=None,)
	state: Optional[ComplianceStatus | str] = Field(alias="state", default=None,)
	userEmail: Optional[str] = Field(alias="userEmail", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .compliance_status import ComplianceStatus
