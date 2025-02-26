from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Norm__s__distPostRequest(BaseModel):
	z: Optional[str] = Field(default=None,alias="z",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


