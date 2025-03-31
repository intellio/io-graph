from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReplacePostRequest(BaseModel):
	oldText: Optional[str] = Field(alias="oldText", default=None,)
	startNum: Optional[str] = Field(alias="startNum", default=None,)
	numChars: Optional[str] = Field(alias="numChars", default=None,)
	newText: Optional[str] = Field(alias="newText", default=None,)

