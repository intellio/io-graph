from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SlnPostRequest(BaseModel):
	cost: Optional[str] = Field(alias="cost", default=None,)
	salvage: Optional[str] = Field(alias="salvage", default=None,)
	life: Optional[str] = Field(alias="life", default=None,)

