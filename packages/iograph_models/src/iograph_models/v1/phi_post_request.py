from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PhiPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)

