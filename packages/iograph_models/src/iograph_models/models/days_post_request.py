from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DaysPostRequest(BaseModel):
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	startDate: Optional[str] = Field(default=None,alias="startDate",)


