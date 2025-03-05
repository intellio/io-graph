from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LearningSelfInitiatedCourse(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	completionPercentage: Optional[int] = Field(alias="completionPercentage",default=None,)
	externalcourseActivityId: Optional[str] = Field(alias="externalcourseActivityId",default=None,)
	learnerUserId: Optional[str] = Field(alias="learnerUserId",default=None,)
	learningContentId: Optional[str] = Field(alias="learningContentId",default=None,)
	learningProviderId: Optional[str] = Field(alias="learningProviderId",default=None,)
	status: Optional[CourseStatus | str] = Field(alias="status",default=None,)
	startedDateTime: Optional[datetime] = Field(alias="startedDateTime",default=None,)

from .course_status import CourseStatus

