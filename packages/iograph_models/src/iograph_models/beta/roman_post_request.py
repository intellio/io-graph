from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RomanPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	form: Optional[str] = Field(alias="form", default=None,)

