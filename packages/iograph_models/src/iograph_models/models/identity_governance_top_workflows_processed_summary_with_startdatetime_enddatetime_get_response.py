from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Identity_governance_top_workflows_processed_summary_with_startdatetime_enddatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[IdentityGovernanceTopWorkflowsInsightsSummary]] = Field(default=None,alias="value",)

from .identity_governance_top_workflows_insights_summary import IdentityGovernanceTopWorkflowsInsightsSummary

