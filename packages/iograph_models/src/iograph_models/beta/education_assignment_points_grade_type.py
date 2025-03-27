from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentPointsGradeType(BaseModel):
	odata_type: Literal["#microsoft.graph.educationAssignmentPointsGradeType"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentPointsGradeType")
	maxPoints: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

