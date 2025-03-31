from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class LearningSelfInitiatedCourse(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.learningSelfInitiatedCourse"] = Field(alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	completionPercentage: Optional[int] = Field(alias="completionPercentage", default=None,)
	externalcourseActivityId: Optional[str] = Field(alias="externalcourseActivityId", default=None,)
	learnerUserId: Optional[str] = Field(alias="learnerUserId", default=None,)
	learningContentId: Optional[str] = Field(alias="learningContentId", default=None,)
	learningProviderId: Optional[str] = Field(alias="learningProviderId", default=None,)
	status: Optional[CourseStatus | str] = Field(alias="status", default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime", default=None,)

from .course_status import CourseStatus
