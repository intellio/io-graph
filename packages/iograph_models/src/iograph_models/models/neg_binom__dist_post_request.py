from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Neg_binom__distPostRequest(BaseModel):
	numberF: Optional[str] = Field(alias="numberF",default=None,)
	numberS: Optional[str] = Field(alias="numberS",default=None,)
	probabilityS: Optional[str] = Field(alias="probabilityS",default=None,)
	cumulative: Optional[str] = Field(alias="cumulative",default=None,)


