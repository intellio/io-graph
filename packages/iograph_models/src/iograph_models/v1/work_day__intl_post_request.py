from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Work_day__intlPostRequest(BaseModel):
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	days: Optional[str] = Field(alias="days", default=None,)
	weekend: Optional[str] = Field(alias="weekend", default=None,)
	holidays: Optional[str] = Field(alias="holidays", default=None,)

