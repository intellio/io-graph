from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ErfPostRequest(BaseModel):
	lowerLimit: Optional[str] = Field(alias="lowerLimit", default=None,)
	upperLimit: Optional[str] = Field(alias="upperLimit", default=None,)

