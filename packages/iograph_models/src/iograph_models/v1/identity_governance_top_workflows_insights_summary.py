from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceTopWorkflowsInsightsSummary(BaseModel):
	failedRuns: Optional[int] = Field(alias="failedRuns", default=None,)
	failedUsers: Optional[int] = Field(alias="failedUsers", default=None,)
	successfulRuns: Optional[int] = Field(alias="successfulRuns", default=None,)
	successfulUsers: Optional[int] = Field(alias="successfulUsers", default=None,)
	totalRuns: Optional[int] = Field(alias="totalRuns", default=None,)
	totalUsers: Optional[int] = Field(alias="totalUsers", default=None,)
	workflowCategory: Optional[IdentityGovernanceLifecycleWorkflowCategory | str] = Field(alias="workflowCategory", default=None,)
	workflowDisplayName: Optional[str] = Field(alias="workflowDisplayName", default=None,)
	workflowId: Optional[str] = Field(alias="workflowId", default=None,)
	workflowVersion: Optional[int] = Field(alias="workflowVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .identity_governance_lifecycle_workflow_category import IdentityGovernanceLifecycleWorkflowCategory
