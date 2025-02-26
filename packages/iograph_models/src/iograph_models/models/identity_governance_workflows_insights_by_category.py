from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceWorkflowsInsightsByCategory(BaseModel):
	failedJoinerRuns: Optional[int] = Field(default=None,alias="failedJoinerRuns",)
	failedLeaverRuns: Optional[int] = Field(default=None,alias="failedLeaverRuns",)
	failedMoverRuns: Optional[int] = Field(default=None,alias="failedMoverRuns",)
	successfulJoinerRuns: Optional[int] = Field(default=None,alias="successfulJoinerRuns",)
	successfulLeaverRuns: Optional[int] = Field(default=None,alias="successfulLeaverRuns",)
	successfulMoverRuns: Optional[int] = Field(default=None,alias="successfulMoverRuns",)
	totalJoinerRuns: Optional[int] = Field(default=None,alias="totalJoinerRuns",)
	totalLeaverRuns: Optional[int] = Field(default=None,alias="totalLeaverRuns",)
	totalMoverRuns: Optional[int] = Field(default=None,alias="totalMoverRuns",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


