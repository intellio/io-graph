from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationTeacher(BaseModel):
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	teacherNumber: Optional[str] = Field(alias="teacherNumber", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

