from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignmentFilterEvaluationSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AssignmentFilterEvaluationSummary]] = Field(alias="value", default=None,)

from .assignment_filter_evaluation_summary import AssignmentFilterEvaluationSummary
