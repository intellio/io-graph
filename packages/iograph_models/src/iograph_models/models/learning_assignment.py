from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LearningAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	completionPercentage: Optional[int] = Field(default=None,alias="completionPercentage",)
	externalcourseActivityId: Optional[str] = Field(default=None,alias="externalcourseActivityId",)
	learnerUserId: Optional[str] = Field(default=None,alias="learnerUserId",)
	learningContentId: Optional[str] = Field(default=None,alias="learningContentId",)
	learningProviderId: Optional[str] = Field(default=None,alias="learningProviderId",)
	status: Optional[CourseStatus] = Field(default=None,alias="status",)
	assignedDateTime: Optional[datetime] = Field(default=None,alias="assignedDateTime",)
	assignerUserId: Optional[str] = Field(default=None,alias="assignerUserId",)
	assignmentType: Optional[AssignmentType] = Field(default=None,alias="assignmentType",)
	dueDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="dueDateTime",)
	notes: Optional[ItemBody] = Field(default=None,alias="notes",)

from .course_status import CourseStatus
from .assignment_type import AssignmentType
from .date_time_time_zone import DateTimeTimeZone
from .item_body import ItemBody

