from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Work_day__intlPostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	days: Optional[str] = Field(default=None,alias="days",)
	weekend: Optional[str] = Field(default=None,alias="weekend",)
	holidays: Optional[str] = Field(default=None,alias="holidays",)


