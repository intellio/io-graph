from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Poisson__distPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	mean: Optional[str] = Field(alias="mean", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)


