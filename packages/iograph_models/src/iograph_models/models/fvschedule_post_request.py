from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FvschedulePostRequest(BaseModel):
	principal: Optional[str] = Field(default=None,alias="principal",)
	schedule: Optional[str] = Field(default=None,alias="schedule",)


