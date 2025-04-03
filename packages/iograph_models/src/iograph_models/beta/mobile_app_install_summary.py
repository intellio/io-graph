from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MobileAppInstallSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppInstallSummary"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppInstallSummary")
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)
	failedUserCount: Optional[int] = Field(alias="failedUserCount", default=None,)
	installedDeviceCount: Optional[int] = Field(alias="installedDeviceCount", default=None,)
	installedUserCount: Optional[int] = Field(alias="installedUserCount", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	notApplicableUserCount: Optional[int] = Field(alias="notApplicableUserCount", default=None,)
	notInstalledDeviceCount: Optional[int] = Field(alias="notInstalledDeviceCount", default=None,)
	notInstalledUserCount: Optional[int] = Field(alias="notInstalledUserCount", default=None,)
	pendingInstallDeviceCount: Optional[int] = Field(alias="pendingInstallDeviceCount", default=None,)
	pendingInstallUserCount: Optional[int] = Field(alias="pendingInstallUserCount", default=None,)

