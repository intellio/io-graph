from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	submissionAnimationDisabled: Optional[bool] = Field(alias="submissionAnimationDisabled",default=None,)
	gradingCategories: Optional[list[EducationGradingCategory]] = Field(alias="gradingCategories",default=None,)

from .education_grading_category import EducationGradingCategory

