from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Identity_governance_top_tasks_processed_summary_with_startdatetime_enddatetimeGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IdentityGovernanceTopTasksInsightsSummary]] = Field(alias="value", default=None,)

from .identity_governance_top_tasks_insights_summary import IdentityGovernanceTopTasksInsightsSummary
