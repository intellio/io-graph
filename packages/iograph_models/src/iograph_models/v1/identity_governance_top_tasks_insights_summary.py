from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTopTasksInsightsSummary(BaseModel):
	failedTasks: Optional[int] = Field(alias="failedTasks", default=None,)
	failedUsers: Optional[int] = Field(alias="failedUsers", default=None,)
	successfulTasks: Optional[int] = Field(alias="successfulTasks", default=None,)
	successfulUsers: Optional[int] = Field(alias="successfulUsers", default=None,)
	taskDefinitionDisplayName: Optional[str] = Field(alias="taskDefinitionDisplayName", default=None,)
	taskDefinitionId: Optional[str] = Field(alias="taskDefinitionId", default=None,)
	totalTasks: Optional[int] = Field(alias="totalTasks", default=None,)
	totalUsers: Optional[int] = Field(alias="totalUsers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


