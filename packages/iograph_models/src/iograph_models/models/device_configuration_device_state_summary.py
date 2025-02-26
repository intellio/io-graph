from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceConfigurationDeviceStateSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	compliantDeviceCount: Optional[int] = Field(default=None,alias="compliantDeviceCount",)
	conflictDeviceCount: Optional[int] = Field(default=None,alias="conflictDeviceCount",)
	errorDeviceCount: Optional[int] = Field(default=None,alias="errorDeviceCount",)
	nonCompliantDeviceCount: Optional[int] = Field(default=None,alias="nonCompliantDeviceCount",)
	notApplicableDeviceCount: Optional[int] = Field(default=None,alias="notApplicableDeviceCount",)
	remediatedDeviceCount: Optional[int] = Field(default=None,alias="remediatedDeviceCount",)
	unknownDeviceCount: Optional[int] = Field(default=None,alias="unknownDeviceCount",)


