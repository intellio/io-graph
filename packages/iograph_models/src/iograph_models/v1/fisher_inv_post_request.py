from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Fisher_invPostRequest(BaseModel):
	y: Optional[str] = Field(alias="y", default=None,)

