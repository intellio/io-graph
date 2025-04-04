from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TextPostRequest(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)
	formatText: Optional[str] = Field(alias="formatText", default=None,)

