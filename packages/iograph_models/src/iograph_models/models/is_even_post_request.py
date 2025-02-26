from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Is_evenPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)


