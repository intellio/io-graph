from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Log_norm__invPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	mean: Optional[str] = Field(default=None,alias="mean",)
	standardDev: Optional[str] = Field(default=None,alias="standardDev",)


