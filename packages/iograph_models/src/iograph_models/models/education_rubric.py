from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationRubric(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[EducationItemBody] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	grading: Optional[EducationAssignmentGradeType] = Field(default=None,alias="grading",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	levels: list[RubricLevel] = Field(alias="levels",)
	qualities: list[RubricQuality] = Field(alias="qualities",)

from .identity_set import IdentitySet
from .education_item_body import EducationItemBody
from .education_assignment_grade_type import EducationAssignmentGradeType
from .identity_set import IdentitySet
from .rubric_level import RubricLevel
from .rubric_quality import RubricQuality

