from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Replace_bPostRequest(BaseModel):
	oldText: Optional[str] = Field(alias="oldText", default=None,)
	startNum: Optional[str] = Field(alias="startNum", default=None,)
	numBytes: Optional[str] = Field(alias="numBytes", default=None,)
	newText: Optional[str] = Field(alias="newText", default=None,)


