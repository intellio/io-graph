from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptRunSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	detectionScriptErrorDeviceCount: Optional[int] = Field(alias="detectionScriptErrorDeviceCount",default=None,)
	detectionScriptNotApplicableDeviceCount: Optional[int] = Field(alias="detectionScriptNotApplicableDeviceCount",default=None,)
	detectionScriptPendingDeviceCount: Optional[int] = Field(alias="detectionScriptPendingDeviceCount",default=None,)
	issueDetectedDeviceCount: Optional[int] = Field(alias="issueDetectedDeviceCount",default=None,)
	issueRemediatedCumulativeDeviceCount: Optional[int] = Field(alias="issueRemediatedCumulativeDeviceCount",default=None,)
	issueRemediatedDeviceCount: Optional[int] = Field(alias="issueRemediatedDeviceCount",default=None,)
	issueReoccurredDeviceCount: Optional[int] = Field(alias="issueReoccurredDeviceCount",default=None,)
	lastScriptRunDateTime: Optional[datetime] = Field(alias="lastScriptRunDateTime",default=None,)
	noIssueDetectedDeviceCount: Optional[int] = Field(alias="noIssueDetectedDeviceCount",default=None,)
	remediationScriptErrorDeviceCount: Optional[int] = Field(alias="remediationScriptErrorDeviceCount",default=None,)
	remediationSkippedDeviceCount: Optional[int] = Field(alias="remediationSkippedDeviceCount",default=None,)


