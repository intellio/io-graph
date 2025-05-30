from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class HardwareConfigurationUserState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hardwareConfigurationUserState"] = Field(alias="@odata.type", default="#microsoft.graph.hardwareConfigurationUserState")
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)
	lastStateUpdateDateTime: Optional[datetime] = Field(alias="lastStateUpdateDateTime", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	pendingDeviceCount: Optional[int] = Field(alias="pendingDeviceCount", default=None,)
	successfulDeviceCount: Optional[int] = Field(alias="successfulDeviceCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)
	upn: Optional[str] = Field(alias="upn", default=None,)
	userEmail: Optional[str] = Field(alias="userEmail", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

