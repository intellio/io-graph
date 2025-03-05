from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Series_sumPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	n: Optional[str] = Field(default=None,alias="n",)
	m: Optional[str] = Field(default=None,alias="m",)
	coefficients: Optional[str] = Field(default=None,alias="coefficients",)


