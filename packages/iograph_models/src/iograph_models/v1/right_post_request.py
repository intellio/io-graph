from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RightPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)
	numChars: Optional[str] = Field(alias="numChars", default=None,)

