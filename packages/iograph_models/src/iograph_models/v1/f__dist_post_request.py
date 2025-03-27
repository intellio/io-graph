from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class F__distPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	degFreedom1: Optional[str] = Field(alias="degFreedom1", default=None,)
	degFreedom2: Optional[str] = Field(alias="degFreedom2", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)


