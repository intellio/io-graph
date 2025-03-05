from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExactPostRequest(BaseModel):
	text1: Optional[str] = Field(alias="text1",default=None,)
	text2: Optional[str] = Field(alias="text2",default=None,)


