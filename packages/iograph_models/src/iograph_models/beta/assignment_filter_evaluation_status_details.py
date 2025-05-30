from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AssignmentFilterEvaluationStatusDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.assignmentFilterEvaluationStatusDetails"] = Field(alias="@odata.type", default="#microsoft.graph.assignmentFilterEvaluationStatusDetails")
	payloadId: Optional[str] = Field(alias="payloadId", default=None,)

