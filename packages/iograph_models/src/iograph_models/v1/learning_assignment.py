from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class LearningAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.learningAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.learningAssignment")
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	completionPercentage: Optional[int] = Field(alias="completionPercentage", default=None,)
	externalcourseActivityId: Optional[str] = Field(alias="externalcourseActivityId", default=None,)
	learnerUserId: Optional[str] = Field(alias="learnerUserId", default=None,)
	learningContentId: Optional[str] = Field(alias="learningContentId", default=None,)
	learningProviderId: Optional[str] = Field(alias="learningProviderId", default=None,)
	status: Optional[CourseStatus | str] = Field(alias="status", default=None,)
	assignedDateTime: Optional[datetime] = Field(alias="assignedDateTime", default=None,)
	assignerUserId: Optional[str] = Field(alias="assignerUserId", default=None,)
	assignmentType: Optional[AssignmentType | str] = Field(alias="assignmentType", default=None,)
	dueDateTime: Optional[DateTimeTimeZone] = Field(alias="dueDateTime", default=None,)
	notes: Optional[ItemBody] = Field(alias="notes", default=None,)

from .course_status import CourseStatus
from .assignment_type import AssignmentType
from .date_time_time_zone import DateTimeTimeZone
from .item_body import ItemBody
