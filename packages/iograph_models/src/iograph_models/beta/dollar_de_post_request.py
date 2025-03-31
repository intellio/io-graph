from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Dollar_dePostRequest(BaseModel):
	fractionalDollar: Optional[str] = Field(alias="fractionalDollar", default=None,)
	fraction: Optional[str] = Field(alias="fraction", default=None,)

