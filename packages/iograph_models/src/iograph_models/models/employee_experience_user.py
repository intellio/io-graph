from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmployeeExperienceUser(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	learningCourseActivities: SerializeAsAny[Optional[list[LearningCourseActivity]]] = Field(alias="learningCourseActivities",default=None,)

from .learning_course_activity import LearningCourseActivity

