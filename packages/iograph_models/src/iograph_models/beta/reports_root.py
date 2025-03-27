from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReportsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	readingAssignmentSubmissions: Optional[list[ReadingAssignmentSubmission]] = Field(alias="readingAssignmentSubmissions", default=None,)
	reflectCheckInResponses: Optional[list[ReflectCheckInResponse]] = Field(alias="reflectCheckInResponses", default=None,)

from .reading_assignment_submission import ReadingAssignmentSubmission
from .reflect_check_in_response import ReflectCheckInResponse

