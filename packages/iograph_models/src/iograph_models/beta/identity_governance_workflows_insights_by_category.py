from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceWorkflowsInsightsByCategory(BaseModel):
	failedJoinerRuns: Optional[int] = Field(alias="failedJoinerRuns", default=None,)
	failedLeaverRuns: Optional[int] = Field(alias="failedLeaverRuns", default=None,)
	failedMoverRuns: Optional[int] = Field(alias="failedMoverRuns", default=None,)
	successfulJoinerRuns: Optional[int] = Field(alias="successfulJoinerRuns", default=None,)
	successfulLeaverRuns: Optional[int] = Field(alias="successfulLeaverRuns", default=None,)
	successfulMoverRuns: Optional[int] = Field(alias="successfulMoverRuns", default=None,)
	totalJoinerRuns: Optional[int] = Field(alias="totalJoinerRuns", default=None,)
	totalLeaverRuns: Optional[int] = Field(alias="totalLeaverRuns", default=None,)
	totalMoverRuns: Optional[int] = Field(alias="totalMoverRuns", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


