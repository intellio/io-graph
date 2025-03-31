from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationGradingScheme(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationGradingScheme"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	grades: Optional[list[EducationGradingSchemeGrade]] = Field(alias="grades", default=None,)
	hidePointsDuringGrading: Optional[bool] = Field(alias="hidePointsDuringGrading", default=None,)

from .education_grading_scheme_grade import EducationGradingSchemeGrade
