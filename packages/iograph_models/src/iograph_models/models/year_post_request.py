from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class YearPostRequest(BaseModel):
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)


