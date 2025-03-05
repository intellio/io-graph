from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationTerm(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


