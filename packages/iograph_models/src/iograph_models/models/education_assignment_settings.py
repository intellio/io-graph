from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationAssignmentSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	submissionAnimationDisabled: Optional[bool] = Field(default=None,alias="submissionAnimationDisabled",)
	gradingCategories: list[EducationGradingCategory] = Field(alias="gradingCategories",)

from .education_grading_category import EducationGradingCategory

