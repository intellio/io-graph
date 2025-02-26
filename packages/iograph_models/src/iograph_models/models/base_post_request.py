from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BasePostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	radix: Optional[str] = Field(default=None,alias="radix",)
	minLength: Optional[str] = Field(default=None,alias="minLength",)


