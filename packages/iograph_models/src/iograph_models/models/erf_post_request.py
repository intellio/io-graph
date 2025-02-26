from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ErfPostRequest(BaseModel):
	lowerLimit: Optional[str] = Field(default=None,alias="lowerLimit",)
	upperLimit: Optional[str] = Field(default=None,alias="upperLimit",)


