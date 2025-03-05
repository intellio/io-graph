from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentDefaults(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	addedStudentAction: Optional[EducationAddedStudentAction] = Field(default=None,alias="addedStudentAction",)
	addToCalendarAction: Optional[EducationAddToCalendarOptions] = Field(default=None,alias="addToCalendarAction",)
	dueTime: Optional[str] = Field(default=None,alias="dueTime",)
	notificationChannelUrl: Optional[str] = Field(default=None,alias="notificationChannelUrl",)

from .education_added_student_action import EducationAddedStudentAction
from .education_add_to_calendar_options import EducationAddToCalendarOptions

