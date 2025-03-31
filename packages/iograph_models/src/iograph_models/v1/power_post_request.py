from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PowerPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	power: Optional[str] = Field(alias="power", default=None,)

