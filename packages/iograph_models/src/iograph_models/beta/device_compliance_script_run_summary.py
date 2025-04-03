from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceComplianceScriptRunSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceComplianceScriptRunSummary"] = Field(alias="@odata.type", default="#microsoft.graph.deviceComplianceScriptRunSummary")
	detectionScriptErrorDeviceCount: Optional[int] = Field(alias="detectionScriptErrorDeviceCount", default=None,)
	detectionScriptPendingDeviceCount: Optional[int] = Field(alias="detectionScriptPendingDeviceCount", default=None,)
	issueDetectedDeviceCount: Optional[int] = Field(alias="issueDetectedDeviceCount", default=None,)
	lastScriptRunDateTime: Optional[datetime] = Field(alias="lastScriptRunDateTime", default=None,)
	noIssueDetectedDeviceCount: Optional[int] = Field(alias="noIssueDetectedDeviceCount", default=None,)

