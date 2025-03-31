from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationTerm(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

