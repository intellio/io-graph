from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceHealthScriptRemediationHistoryData(BaseModel):
	date: Optional[str] = Field(alias="date", default=None,)
	detectFailedDeviceCount: Optional[int] = Field(alias="detectFailedDeviceCount", default=None,)
	noIssueDeviceCount: Optional[int] = Field(alias="noIssueDeviceCount", default=None,)
	remediatedDeviceCount: Optional[int] = Field(alias="remediatedDeviceCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


