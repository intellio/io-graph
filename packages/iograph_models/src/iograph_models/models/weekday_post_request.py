from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WeekdayPostRequest(BaseModel):
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	returnType: Optional[str] = Field(default=None,alias="returnType",)


