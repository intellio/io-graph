from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Evaluate_assignment_filterPostRequest(BaseModel):
	data: Optional[AssignmentFilterEvaluateRequest] = Field(alias="data",default=None,)

from .assignment_filter_evaluate_request import AssignmentFilterEvaluateRequest

