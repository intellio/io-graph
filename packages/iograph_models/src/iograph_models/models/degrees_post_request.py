from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DegreesPostRequest(BaseModel):
	angle: Optional[str] = Field(default=None,alias="angle",)


