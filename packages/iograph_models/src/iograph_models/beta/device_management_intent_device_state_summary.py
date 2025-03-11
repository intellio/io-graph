from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentDeviceStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	conflictCount: Optional[int] = Field(alias="conflictCount",default=None,)
	errorCount: Optional[int] = Field(alias="errorCount",default=None,)
	failedCount: Optional[int] = Field(alias="failedCount",default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount",default=None,)
	notApplicablePlatformCount: Optional[int] = Field(alias="notApplicablePlatformCount",default=None,)
	successCount: Optional[int] = Field(alias="successCount",default=None,)


