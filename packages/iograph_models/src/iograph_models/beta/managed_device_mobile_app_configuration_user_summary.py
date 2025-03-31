from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedDeviceMobileAppConfigurationUserSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary"] = Field(alias="@odata.type",)
	configurationVersion: Optional[int] = Field(alias="configurationVersion", default=None,)
	conflictCount: Optional[int] = Field(alias="conflictCount", default=None,)
	errorCount: Optional[int] = Field(alias="errorCount", default=None,)
	failedCount: Optional[int] = Field(alias="failedCount", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount", default=None,)
	pendingCount: Optional[int] = Field(alias="pendingCount", default=None,)
	successCount: Optional[int] = Field(alias="successCount", default=None,)

