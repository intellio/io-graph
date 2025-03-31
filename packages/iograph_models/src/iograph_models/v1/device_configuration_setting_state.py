from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceConfigurationSettingState(BaseModel):
	currentValue: Optional[str] = Field(alias="currentValue", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	errorDescription: Optional[str] = Field(alias="errorDescription", default=None,)
	instanceDisplayName: Optional[str] = Field(alias="instanceDisplayName", default=None,)
	setting: Optional[str] = Field(alias="setting", default=None,)
	settingName: Optional[str] = Field(alias="settingName", default=None,)
	sources: Optional[list[SettingSource]] = Field(alias="sources", default=None,)
	state: Optional[ComplianceStatus | str] = Field(alias="state", default=None,)
	userEmail: Optional[str] = Field(alias="userEmail", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .setting_source import SettingSource
from .compliance_status import ComplianceStatus
