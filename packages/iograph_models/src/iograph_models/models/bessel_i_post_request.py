from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Bessel_iPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	n: Optional[str] = Field(default=None,alias="n",)


