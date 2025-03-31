from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Erf_c__precisePostRequest(BaseModel):
	X: Optional[str] = Field(alias="X", default=None,)

