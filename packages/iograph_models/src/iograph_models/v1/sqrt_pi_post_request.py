from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Sqrt_piPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)

