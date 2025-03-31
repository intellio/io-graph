from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Binom__distPostRequest(BaseModel):
	numberS: Optional[str] = Field(alias="numberS", default=None,)
	trials: Optional[str] = Field(alias="trials", default=None,)
	probabilityS: Optional[str] = Field(alias="probabilityS", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)

