from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationCourse(BaseModel):
	courseNumber: Optional[str] = Field(default=None,alias="courseNumber",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


