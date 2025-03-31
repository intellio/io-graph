from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationalActivityDetail(BaseModel):
	abbreviation: Optional[str] = Field(alias="abbreviation", default=None,)
	activities: Optional[list[str]] = Field(alias="activities", default=None,)
	awards: Optional[list[str]] = Field(alias="awards", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fieldsOfStudy: Optional[list[str]] = Field(alias="fieldsOfStudy", default=None,)
	grade: Optional[str] = Field(alias="grade", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

