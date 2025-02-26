from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MroundPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	multiple: Optional[str] = Field(default=None,alias="multiple",)


