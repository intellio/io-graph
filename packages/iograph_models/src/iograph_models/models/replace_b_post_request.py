from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Replace_bPostRequest(BaseModel):
	oldText: Optional[str] = Field(default=None,alias="oldText",)
	startNum: Optional[str] = Field(default=None,alias="startNum",)
	numBytes: Optional[str] = Field(default=None,alias="numBytes",)
	newText: Optional[str] = Field(default=None,alias="newText",)


