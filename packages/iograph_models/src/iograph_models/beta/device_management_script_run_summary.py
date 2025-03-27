from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementScriptRunSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	errorUserCount: Optional[int] = Field(alias="errorUserCount", default=None,)
	successDeviceCount: Optional[int] = Field(alias="successDeviceCount", default=None,)
	successUserCount: Optional[int] = Field(alias="successUserCount", default=None,)


