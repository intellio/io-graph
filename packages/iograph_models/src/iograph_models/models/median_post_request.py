from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MedianPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)


