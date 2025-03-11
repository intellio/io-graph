from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationPointsOutcome(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	points: Optional[EducationAssignmentPointsGrade] = Field(alias="points",default=None,)
	publishedPoints: Optional[EducationAssignmentPointsGrade] = Field(alias="publishedPoints",default=None,)

from .identity_set import IdentitySet
from .education_assignment_points_grade import EducationAssignmentPointsGrade
from .education_assignment_points_grade import EducationAssignmentPointsGrade

