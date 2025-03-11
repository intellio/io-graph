from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Binom__invPostRequest(BaseModel):
	trials: Optional[str] = Field(alias="trials",default=None,)
	probabilityS: Optional[str] = Field(alias="probabilityS",default=None,)
	alpha: Optional[str] = Field(alias="alpha",default=None,)


