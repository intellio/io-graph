from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Find_bPostRequest(BaseModel):
	findText: Optional[str] = Field(default=None,alias="findText",)
	withinText: Optional[str] = Field(default=None,alias="withinText",)
	startNum: Optional[str] = Field(default=None,alias="startNum",)


