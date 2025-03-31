from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SoftwareUpdateStatusSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.softwareUpdateStatusSummary"] = Field(alias="@odata.type",)
	compliantDeviceCount: Optional[int] = Field(alias="compliantDeviceCount", default=None,)
	compliantUserCount: Optional[int] = Field(alias="compliantUserCount", default=None,)
	conflictDeviceCount: Optional[int] = Field(alias="conflictDeviceCount", default=None,)
	conflictUserCount: Optional[int] = Field(alias="conflictUserCount", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	errorUserCount: Optional[int] = Field(alias="errorUserCount", default=None,)
	nonCompliantDeviceCount: Optional[int] = Field(alias="nonCompliantDeviceCount", default=None,)
	nonCompliantUserCount: Optional[int] = Field(alias="nonCompliantUserCount", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	notApplicableUserCount: Optional[int] = Field(alias="notApplicableUserCount", default=None,)
	remediatedDeviceCount: Optional[int] = Field(alias="remediatedDeviceCount", default=None,)
	remediatedUserCount: Optional[int] = Field(alias="remediatedUserCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)
	unknownUserCount: Optional[int] = Field(alias="unknownUserCount", default=None,)

