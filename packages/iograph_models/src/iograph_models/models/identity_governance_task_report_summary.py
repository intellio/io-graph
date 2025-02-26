from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTaskReportSummary(BaseModel):
	failedTasks: Optional[int] = Field(default=None,alias="failedTasks",)
	successfulTasks: Optional[int] = Field(default=None,alias="successfulTasks",)
	totalTasks: Optional[int] = Field(default=None,alias="totalTasks",)
	unprocessedTasks: Optional[int] = Field(default=None,alias="unprocessedTasks",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


