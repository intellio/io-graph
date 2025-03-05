from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Set_positionPostRequest(BaseModel):
	startCell: Optional[str] = Field(default=None,alias="startCell",)
	endCell: Optional[str] = Field(default=None,alias="endCell",)


