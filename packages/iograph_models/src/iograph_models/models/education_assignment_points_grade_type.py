from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationAssignmentPointsGradeType(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	maxPoints: Optional[float] | Optional[str] | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

