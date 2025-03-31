from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubtotalPostRequest(BaseModel):
	functionNum: Optional[str] = Field(alias="functionNum", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)

