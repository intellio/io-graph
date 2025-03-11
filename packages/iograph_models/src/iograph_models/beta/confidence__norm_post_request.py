from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Confidence__normPostRequest(BaseModel):
	alpha: Optional[str] = Field(alias="alpha",default=None,)
	standardDev: Optional[str] = Field(alias="standardDev",default=None,)
	size: Optional[str] = Field(alias="size",default=None,)


