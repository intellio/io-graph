from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Is_non_textPostRequest(BaseModel):
	value: Optional[str] = Field(default=None,alias="value",)


