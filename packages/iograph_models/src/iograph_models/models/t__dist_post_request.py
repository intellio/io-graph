from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class T__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	degFreedom: Optional[str] = Field(default=None,alias="degFreedom",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


