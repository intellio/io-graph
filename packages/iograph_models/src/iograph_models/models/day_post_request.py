from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DayPostRequest(BaseModel):
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)


