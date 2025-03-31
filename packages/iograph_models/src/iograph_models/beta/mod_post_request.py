from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ModPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	divisor: Optional[str] = Field(alias="divisor", default=None,)

