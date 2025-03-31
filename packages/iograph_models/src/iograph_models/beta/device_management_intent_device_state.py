from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementIntentDeviceState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementIntentDeviceState"] = Field(alias="@odata.type",)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	state: Optional[ComplianceStatus | str] = Field(alias="state", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .compliance_status import ComplianceStatus
