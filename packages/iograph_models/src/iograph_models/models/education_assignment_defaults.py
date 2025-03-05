from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentDefaults(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	addedStudentAction: Optional[str | EducationAddedStudentAction] = Field(alias="addedStudentAction",default=None,)
	addToCalendarAction: Optional[str | EducationAddToCalendarOptions] = Field(alias="addToCalendarAction",default=None,)
	dueTime: Optional[str] = Field(alias="dueTime",default=None,)
	notificationChannelUrl: Optional[str] = Field(alias="notificationChannelUrl",default=None,)

from .education_added_student_action import EducationAddedStudentAction
from .education_add_to_calendar_options import EducationAddToCalendarOptions

