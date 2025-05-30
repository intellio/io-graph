from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Find_bPostRequest(BaseModel):
	findText: Optional[str] = Field(alias="findText", default=None,)
	withinText: Optional[str] = Field(alias="withinText", default=None,)
	startNum: Optional[str] = Field(alias="startNum", default=None,)

