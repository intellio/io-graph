from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MidbPostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)
	startNum: Optional[str] = Field(default=None,alias="startNum",)
	numBytes: Optional[str] = Field(default=None,alias="numBytes",)


