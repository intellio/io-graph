from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceConfigurationUserOverview(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configurationVersion: Optional[int] = Field(default=None,alias="configurationVersion",)
	errorCount: Optional[int] = Field(default=None,alias="errorCount",)
	failedCount: Optional[int] = Field(default=None,alias="failedCount",)
	lastUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastUpdateDateTime",)
	notApplicableCount: Optional[int] = Field(default=None,alias="notApplicableCount",)
	pendingCount: Optional[int] = Field(default=None,alias="pendingCount",)
	successCount: Optional[int] = Field(default=None,alias="successCount",)


