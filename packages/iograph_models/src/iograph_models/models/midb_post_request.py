from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MidbPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text",default=None,)
	startNum: Optional[str] = Field(alias="startNum",default=None,)
	numBytes: Optional[str] = Field(alias="numBytes",default=None,)


