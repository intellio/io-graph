from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentDeviceSettingStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	compliantCount: Optional[int] = Field(alias="compliantCount",default=None,)
	conflictCount: Optional[int] = Field(alias="conflictCount",default=None,)
	errorCount: Optional[int] = Field(alias="errorCount",default=None,)
	nonCompliantCount: Optional[int] = Field(alias="nonCompliantCount",default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount",default=None,)
	remediatedCount: Optional[int] = Field(alias="remediatedCount",default=None,)
	settingName: Optional[str] = Field(alias="settingName",default=None,)


