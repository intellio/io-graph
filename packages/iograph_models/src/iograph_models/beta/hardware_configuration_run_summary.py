from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class HardwareConfigurationRunSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	errorUserCount: Optional[int] = Field(alias="errorUserCount", default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)
	failedUserCount: Optional[int] = Field(alias="failedUserCount", default=None,)
	lastRunDateTime: Optional[datetime] = Field(alias="lastRunDateTime", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	notApplicableUserCount: Optional[int] = Field(alias="notApplicableUserCount", default=None,)
	pendingDeviceCount: Optional[int] = Field(alias="pendingDeviceCount", default=None,)
	pendingUserCount: Optional[int] = Field(alias="pendingUserCount", default=None,)
	successfulDeviceCount: Optional[int] = Field(alias="successfulDeviceCount", default=None,)
	successfulUserCount: Optional[int] = Field(alias="successfulUserCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)
	unknownUserCount: Optional[int] = Field(alias="unknownUserCount", default=None,)


