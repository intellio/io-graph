from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Days360PostRequest(BaseModel):
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	method: Optional[str] = Field(alias="method", default=None,)

