from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LogPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	base: Optional[str] = Field(alias="base", default=None,)

