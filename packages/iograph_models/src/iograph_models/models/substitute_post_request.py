from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubstitutePostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)
	oldText: Optional[str] = Field(default=None,alias="oldText",)
	newText: Optional[str] = Field(default=None,alias="newText",)
	instanceNum: Optional[str] = Field(default=None,alias="instanceNum",)


