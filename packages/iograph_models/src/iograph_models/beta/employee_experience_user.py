from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class EmployeeExperienceUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.employeeExperienceUser"] = Field(alias="@odata.type", default="#microsoft.graph.employeeExperienceUser")
	learningCourseActivities: Optional[list[Annotated[Union[LearningAssignment, LearningSelfInitiatedCourse],Field(discriminator="odata_type")]]] = Field(alias="learningCourseActivities", default=None,)

from .learning_assignment import LearningAssignment
from .learning_self_initiated_course import LearningSelfInitiatedCourse
