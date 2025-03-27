from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Series_sumPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	n: Optional[str] = Field(alias="n", default=None,)
	m: Optional[str] = Field(alias="m", default=None,)
	coefficients: Optional[str] = Field(alias="coefficients", default=None,)


