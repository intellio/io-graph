from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceRunSummary(BaseModel):
	failedRuns: Optional[int] = Field(alias="failedRuns", default=None,)
	failedTasks: Optional[int] = Field(alias="failedTasks", default=None,)
	successfulRuns: Optional[int] = Field(alias="successfulRuns", default=None,)
	totalRuns: Optional[int] = Field(alias="totalRuns", default=None,)
	totalTasks: Optional[int] = Field(alias="totalTasks", default=None,)
	totalUsers: Optional[int] = Field(alias="totalUsers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

