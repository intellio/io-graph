from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationCourse(BaseModel):
	courseNumber: Optional[str] = Field(alias="courseNumber", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

