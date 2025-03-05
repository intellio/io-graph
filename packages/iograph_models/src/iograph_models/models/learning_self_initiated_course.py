from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LearningSelfInitiatedCourse(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	completionPercentage: Optional[int] = Field(default=None,alias="completionPercentage",)
	externalcourseActivityId: Optional[str] = Field(default=None,alias="externalcourseActivityId",)
	learnerUserId: Optional[str] = Field(default=None,alias="learnerUserId",)
	learningContentId: Optional[str] = Field(default=None,alias="learningContentId",)
	learningProviderId: Optional[str] = Field(default=None,alias="learningProviderId",)
	status: Optional[CourseStatus] = Field(default=None,alias="status",)
	startedDateTime: Optional[datetime] = Field(default=None,alias="startedDateTime",)

from .course_status import CourseStatus

