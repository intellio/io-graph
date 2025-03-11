from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Binom__dist__rangePostRequest(BaseModel):
	trials: Optional[str] = Field(alias="trials",default=None,)
	probabilityS: Optional[str] = Field(alias="probabilityS",default=None,)
	numberS: Optional[str] = Field(alias="numberS",default=None,)
	numberS2: Optional[str] = Field(alias="numberS2",default=None,)


