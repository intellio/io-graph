from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Ge_stepPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	step: Optional[str] = Field(default=None,alias="step",)


