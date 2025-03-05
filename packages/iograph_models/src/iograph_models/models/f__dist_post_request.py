from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class F__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	degFreedom1: Optional[str] = Field(default=None,alias="degFreedom1",)
	degFreedom2: Optional[str] = Field(default=None,alias="degFreedom2",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


