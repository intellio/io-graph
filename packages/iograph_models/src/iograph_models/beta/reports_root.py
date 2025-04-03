from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ReportsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.reportsRoot"] = Field(alias="@odata.type", default="#microsoft.graph.reportsRoot")
	readingAssignmentSubmissions: Optional[list[ReadingAssignmentSubmission]] = Field(alias="readingAssignmentSubmissions", default=None,)
	reflectCheckInResponses: Optional[list[ReflectCheckInResponse]] = Field(alias="reflectCheckInResponses", default=None,)

from .reading_assignment_submission import ReadingAssignmentSubmission
from .reflect_check_in_response import ReflectCheckInResponse
