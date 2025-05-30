from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceConfigurationDeviceOverview(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceConfigurationDeviceOverview"] = Field(alias="@odata.type", default="#microsoft.graph.deviceConfigurationDeviceOverview")
	configurationVersion: Optional[int] = Field(alias="configurationVersion", default=None,)
	errorCount: Optional[int] = Field(alias="errorCount", default=None,)
	failedCount: Optional[int] = Field(alias="failedCount", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount", default=None,)
	pendingCount: Optional[int] = Field(alias="pendingCount", default=None,)
	successCount: Optional[int] = Field(alias="successCount", default=None,)

