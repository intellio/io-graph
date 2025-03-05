from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MidPostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)
	startNum: Optional[str] = Field(default=None,alias="startNum",)
	numChars: Optional[str] = Field(default=None,alias="numChars",)


