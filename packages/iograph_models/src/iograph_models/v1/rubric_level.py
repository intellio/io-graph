from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class RubricLevel(BaseModel):
	description: Optional[EducationItemBody] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	grading: Optional[Union[EducationAssignmentPointsGradeType]] = Field(alias="grading", default=None,discriminator="odata_type", )
	levelId: Optional[str] = Field(alias="levelId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .education_item_body import EducationItemBody
from .education_assignment_points_grade_type import EducationAssignmentPointsGradeType
