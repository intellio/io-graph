from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IrrPostRequest(BaseModel):
	values: Optional[str] = Field(alias="values", default=None,)
	guess: Optional[str] = Field(alias="guess", default=None,)

