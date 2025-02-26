from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RubricLevel(BaseModel):
	description: Optional[EducationItemBody] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	grading: Optional[EducationAssignmentGradeType] = Field(default=None,alias="grading",)
	levelId: Optional[str] = Field(default=None,alias="levelId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .education_item_body import EducationItemBody
from .education_assignment_grade_type import EducationAssignmentGradeType

