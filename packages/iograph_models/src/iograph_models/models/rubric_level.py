from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricLevel(BaseModel):
	description: Optional[EducationItemBody] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	grading: SerializeAsAny[Optional[EducationAssignmentGradeType]] = Field(alias="grading",default=None,)
	levelId: Optional[str] = Field(alias="levelId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .education_item_body import EducationItemBody
from .education_assignment_grade_type import EducationAssignmentGradeType

