from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StandardizePostRequest(BaseModel):
	x: Optional[str] = Field(alias="x",default=None,)
	mean: Optional[str] = Field(alias="mean",default=None,)
	standardDev: Optional[str] = Field(alias="standardDev",default=None,)


