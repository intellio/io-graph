from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Iso_week_numPostRequest(BaseModel):
	date: Optional[str] = Field(default=None,alias="date",)


