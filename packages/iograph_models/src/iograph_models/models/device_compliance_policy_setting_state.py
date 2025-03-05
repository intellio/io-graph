from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicySettingState(BaseModel):
	currentValue: Optional[str] = Field(default=None,alias="currentValue",)
	errorCode: Optional[int] = Field(default=None,alias="errorCode",)
	errorDescription: Optional[str] = Field(default=None,alias="errorDescription",)
	instanceDisplayName: Optional[str] = Field(default=None,alias="instanceDisplayName",)
	setting: Optional[str] = Field(default=None,alias="setting",)
	settingName: Optional[str] = Field(default=None,alias="settingName",)
	sources: Optional[list[SettingSource]] = Field(default=None,alias="sources",)
	state: Optional[ComplianceStatus] = Field(default=None,alias="state",)
	userEmail: Optional[str] = Field(default=None,alias="userEmail",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	userName: Optional[str] = Field(default=None,alias="userName",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .setting_source import SettingSource
from .compliance_status import ComplianceStatus

