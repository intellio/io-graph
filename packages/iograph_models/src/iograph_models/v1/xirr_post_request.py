from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class XirrPostRequest(BaseModel):
	values: Optional[str] = Field(alias="values", default=None,)
	dates: Optional[str] = Field(alias="dates", default=None,)
	guess: Optional[str] = Field(alias="guess", default=None,)

