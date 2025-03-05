from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LeftPostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)
	numChars: Optional[str] = Field(default=None,alias="numChars",)


