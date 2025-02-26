from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NominalPostRequest(BaseModel):
	effectRate: Optional[str] = Field(default=None,alias="effectRate",)
	npery: Optional[str] = Field(default=None,alias="npery",)


