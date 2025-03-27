from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Z__testPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)
	x: Optional[str] = Field(alias="x", default=None,)
	sigma: Optional[str] = Field(alias="sigma", default=None,)


