from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Network_daysPostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	holidays: Optional[str] = Field(default=None,alias="holidays",)


