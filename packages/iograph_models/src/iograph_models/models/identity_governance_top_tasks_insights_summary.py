from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTopTasksInsightsSummary(BaseModel):
	failedTasks: Optional[int] = Field(default=None,alias="failedTasks",)
	failedUsers: Optional[int] = Field(default=None,alias="failedUsers",)
	successfulTasks: Optional[int] = Field(default=None,alias="successfulTasks",)
	successfulUsers: Optional[int] = Field(default=None,alias="successfulUsers",)
	taskDefinitionDisplayName: Optional[str] = Field(default=None,alias="taskDefinitionDisplayName",)
	taskDefinitionId: Optional[str] = Field(default=None,alias="taskDefinitionId",)
	totalTasks: Optional[int] = Field(default=None,alias="totalTasks",)
	totalUsers: Optional[int] = Field(default=None,alias="totalUsers",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


