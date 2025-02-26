from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Network_days__intlPostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	weekend: Optional[str] = Field(default=None,alias="weekend",)
	holidays: Optional[str] = Field(default=None,alias="holidays",)


