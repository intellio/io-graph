from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Neg_binom__distPostRequest(BaseModel):
	numberF: Optional[str] = Field(default=None,alias="numberF",)
	numberS: Optional[str] = Field(default=None,alias="numberS",)
	probabilityS: Optional[str] = Field(default=None,alias="probabilityS",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


