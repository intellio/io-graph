from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceComplianceScriptRunSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	detectionScriptErrorDeviceCount: Optional[int] = Field(alias="detectionScriptErrorDeviceCount", default=None,)
	detectionScriptPendingDeviceCount: Optional[int] = Field(alias="detectionScriptPendingDeviceCount", default=None,)
	issueDetectedDeviceCount: Optional[int] = Field(alias="issueDetectedDeviceCount", default=None,)
	lastScriptRunDateTime: Optional[datetime] = Field(alias="lastScriptRunDateTime", default=None,)
	noIssueDetectedDeviceCount: Optional[int] = Field(alias="noIssueDetectedDeviceCount", default=None,)


