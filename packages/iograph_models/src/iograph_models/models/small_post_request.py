from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SmallPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	k: Optional[str] = Field(default=None,alias="k",)


