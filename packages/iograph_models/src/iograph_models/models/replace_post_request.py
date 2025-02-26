from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReplacePostRequest(BaseModel):
	oldText: Optional[str] = Field(default=None,alias="oldText",)
	startNum: Optional[str] = Field(default=None,alias="startNum",)
	numChars: Optional[str] = Field(default=None,alias="numChars",)
	newText: Optional[str] = Field(default=None,alias="newText",)


