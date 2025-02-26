from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Days360PostRequest(BaseModel):
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	method: Optional[str] = Field(default=None,alias="method",)


