from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NpvPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)

