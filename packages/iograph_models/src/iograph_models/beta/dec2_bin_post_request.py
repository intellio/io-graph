from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Dec2_binPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	places: Optional[str] = Field(alias="places", default=None,)

