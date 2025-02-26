from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NotPostRequest(BaseModel):
	logical: Optional[str] = Field(default=None,alias="logical",)


