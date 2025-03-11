from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterTypeAndEvaluationResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AssignmentFilterTypeAndEvaluationResult]] = Field(alias="value",default=None,)

from .assignment_filter_type_and_evaluation_result import AssignmentFilterTypeAndEvaluationResult

