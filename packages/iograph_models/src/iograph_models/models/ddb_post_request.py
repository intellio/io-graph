from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DdbPostRequest(BaseModel):
	cost: Optional[str] = Field(default=None,alias="cost",)
	salvage: Optional[str] = Field(default=None,alias="salvage",)
	life: Optional[str] = Field(default=None,alias="life",)
	period: Optional[str] = Field(default=None,alias="period",)
	factor: Optional[str] = Field(default=None,alias="factor",)


