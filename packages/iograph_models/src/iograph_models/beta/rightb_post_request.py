from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RightbPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)
	numBytes: Optional[str] = Field(alias="numBytes", default=None,)


