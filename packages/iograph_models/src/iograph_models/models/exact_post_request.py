from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExactPostRequest(BaseModel):
	text1: Optional[str] = Field(default=None,alias="text1",)
	text2: Optional[str] = Field(default=None,alias="text2",)


