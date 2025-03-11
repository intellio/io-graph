from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflowsInsightsSummary(BaseModel):
	failedRuns: Optional[int] = Field(alias="failedRuns",default=None,)
	failedTasks: Optional[int] = Field(alias="failedTasks",default=None,)
	failedUsers: Optional[int] = Field(alias="failedUsers",default=None,)
	successfulRuns: Optional[int] = Field(alias="successfulRuns",default=None,)
	successfulTasks: Optional[int] = Field(alias="successfulTasks",default=None,)
	successfulUsers: Optional[int] = Field(alias="successfulUsers",default=None,)
	totalRuns: Optional[int] = Field(alias="totalRuns",default=None,)
	totalTasks: Optional[int] = Field(alias="totalTasks",default=None,)
	totalUsers: Optional[int] = Field(alias="totalUsers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


