from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationAssignmentSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentSettings")
	submissionAnimationDisabled: Optional[bool] = Field(alias="submissionAnimationDisabled", default=None,)
	defaultGradingScheme: Optional[EducationGradingScheme] = Field(alias="defaultGradingScheme", default=None,)
	gradingCategories: Optional[list[EducationGradingCategory]] = Field(alias="gradingCategories", default=None,)
	gradingSchemes: Optional[list[EducationGradingScheme]] = Field(alias="gradingSchemes", default=None,)

from .education_grading_scheme import EducationGradingScheme
from .education_grading_category import EducationGradingCategory
