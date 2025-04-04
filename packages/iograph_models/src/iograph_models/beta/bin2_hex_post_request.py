from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bin2_hexPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	places: Optional[str] = Field(alias="places", default=None,)

