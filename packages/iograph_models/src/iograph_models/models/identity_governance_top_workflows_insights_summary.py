from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTopWorkflowsInsightsSummary(BaseModel):
	failedRuns: Optional[int] = Field(default=None,alias="failedRuns",)
	failedUsers: Optional[int] = Field(default=None,alias="failedUsers",)
	successfulRuns: Optional[int] = Field(default=None,alias="successfulRuns",)
	successfulUsers: Optional[int] = Field(default=None,alias="successfulUsers",)
	totalRuns: Optional[int] = Field(default=None,alias="totalRuns",)
	totalUsers: Optional[int] = Field(default=None,alias="totalUsers",)
	workflowCategory: Optional[IdentityGovernanceLifecycleWorkflowCategory] = Field(default=None,alias="workflowCategory",)
	workflowDisplayName: Optional[str] = Field(default=None,alias="workflowDisplayName",)
	workflowId: Optional[str] = Field(default=None,alias="workflowId",)
	workflowVersion: Optional[int] = Field(default=None,alias="workflowVersion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory

