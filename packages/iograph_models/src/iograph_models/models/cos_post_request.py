from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CosPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)


