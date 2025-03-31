from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_positionPostRequest(BaseModel):
	startCell: Optional[str] = Field(alias="startCell", default=None,)
	endCell: Optional[str] = Field(alias="endCell", default=None,)

