from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementIntentUserStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementIntentUserStateSummary"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementIntentUserStateSummary")
	conflictCount: Optional[int] = Field(alias="conflictCount", default=None,)
	errorCount: Optional[int] = Field(alias="errorCount", default=None,)
	failedCount: Optional[int] = Field(alias="failedCount", default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount", default=None,)
	successCount: Optional[int] = Field(alias="successCount", default=None,)

