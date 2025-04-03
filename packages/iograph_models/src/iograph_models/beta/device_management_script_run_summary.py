from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementScriptRunSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementScriptRunSummary"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementScriptRunSummary")
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	errorUserCount: Optional[int] = Field(alias="errorUserCount", default=None,)
	successDeviceCount: Optional[int] = Field(alias="successDeviceCount", default=None,)
	successUserCount: Optional[int] = Field(alias="successUserCount", default=None,)

