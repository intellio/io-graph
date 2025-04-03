from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationAssignmentDefaults(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationAssignmentDefaults"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentDefaults")
	addedStudentAction: Optional[EducationAddedStudentAction | str] = Field(alias="addedStudentAction", default=None,)
	addToCalendarAction: Optional[EducationAddToCalendarOptions | str] = Field(alias="addToCalendarAction", default=None,)
	dueTime: Optional[str] = Field(alias="dueTime", default=None,)
	notificationChannelUrl: Optional[str] = Field(alias="notificationChannelUrl", default=None,)

from .education_added_student_action import EducationAddedStudentAction
from .education_add_to_calendar_options import EducationAddToCalendarOptions
