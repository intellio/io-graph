from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bessel_kPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	n: Optional[str] = Field(alias="n", default=None,)

