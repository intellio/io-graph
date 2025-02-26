from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SoftwareUpdateStatusSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	compliantDeviceCount: Optional[int] = Field(default=None,alias="compliantDeviceCount",)
	compliantUserCount: Optional[int] = Field(default=None,alias="compliantUserCount",)
	conflictDeviceCount: Optional[int] = Field(default=None,alias="conflictDeviceCount",)
	conflictUserCount: Optional[int] = Field(default=None,alias="conflictUserCount",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	errorDeviceCount: Optional[int] = Field(default=None,alias="errorDeviceCount",)
	errorUserCount: Optional[int] = Field(default=None,alias="errorUserCount",)
	nonCompliantDeviceCount: Optional[int] = Field(default=None,alias="nonCompliantDeviceCount",)
	nonCompliantUserCount: Optional[int] = Field(default=None,alias="nonCompliantUserCount",)
	notApplicableDeviceCount: Optional[int] = Field(default=None,alias="notApplicableDeviceCount",)
	notApplicableUserCount: Optional[int] = Field(default=None,alias="notApplicableUserCount",)
	remediatedDeviceCount: Optional[int] = Field(default=None,alias="remediatedDeviceCount",)
	remediatedUserCount: Optional[int] = Field(default=None,alias="remediatedUserCount",)
	unknownDeviceCount: Optional[int] = Field(default=None,alias="unknownDeviceCount",)
	unknownUserCount: Optional[int] = Field(default=None,alias="unknownUserCount",)


