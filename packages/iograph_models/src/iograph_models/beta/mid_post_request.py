from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MidPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)
	startNum: Optional[str] = Field(alias="startNum", default=None,)
	numChars: Optional[str] = Field(alias="numChars", default=None,)

