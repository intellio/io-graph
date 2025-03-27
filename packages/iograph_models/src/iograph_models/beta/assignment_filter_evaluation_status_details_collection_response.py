from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterEvaluationStatusDetailsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AssignmentFilterEvaluationStatusDetails]] = Field(alias="value", default=None,)

from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails

