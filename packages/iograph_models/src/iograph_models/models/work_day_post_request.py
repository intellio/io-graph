from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Work_dayPostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	days: Optional[str] = Field(default=None,alias="days",)
	holidays: Optional[str] = Field(default=None,alias="holidays",)


