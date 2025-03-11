from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SettingStateDeviceSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	compliantDeviceCount: Optional[int] = Field(alias="compliantDeviceCount",default=None,)
	conflictDeviceCount: Optional[int] = Field(alias="conflictDeviceCount",default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount",default=None,)
	instancePath: Optional[str] = Field(alias="instancePath",default=None,)
	nonCompliantDeviceCount: Optional[int] = Field(alias="nonCompliantDeviceCount",default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount",default=None,)
	remediatedDeviceCount: Optional[int] = Field(alias="remediatedDeviceCount",default=None,)
	settingName: Optional[str] = Field(alias="settingName",default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount",default=None,)


