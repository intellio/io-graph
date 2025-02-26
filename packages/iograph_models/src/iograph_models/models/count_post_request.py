from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CountPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)


