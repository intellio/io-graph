from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceConfigurationDeviceStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceConfigurationDeviceStatus"] = Field(alias="@odata.type", default="#microsoft.graph.deviceConfigurationDeviceStatus")
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(alias="complianceGracePeriodExpirationDateTime", default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	status: Optional[ComplianceStatus | str] = Field(alias="status", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .compliance_status import ComplianceStatus
