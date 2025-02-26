from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationPointsOutcome(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	points: Optional[EducationAssignmentPointsGrade] = Field(default=None,alias="points",)
	publishedPoints: Optional[EducationAssignmentPointsGrade] = Field(default=None,alias="publishedPoints",)

from .identity_set import IdentitySet
from .education_assignment_points_grade import EducationAssignmentPointsGrade
from .education_assignment_points_grade import EducationAssignmentPointsGrade

