from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LogPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	base: Optional[str] = Field(default=None,alias="base",)


