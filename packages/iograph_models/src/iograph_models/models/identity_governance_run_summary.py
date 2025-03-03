from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceRunSummary(BaseModel):
	failedRuns: Optional[int] = Field(default=None,alias="failedRuns",)
	failedTasks: Optional[int] = Field(default=None,alias="failedTasks",)
	successfulRuns: Optional[int] = Field(default=None,alias="successfulRuns",)
	totalRuns: Optional[int] = Field(default=None,alias="totalRuns",)
	totalTasks: Optional[int] = Field(default=None,alias="totalTasks",)
	totalUsers: Optional[int] = Field(default=None,alias="totalUsers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


