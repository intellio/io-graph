from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EffectPostRequest(BaseModel):
	nominalRate: Optional[str] = Field(alias="nominalRate", default=None,)
	npery: Optional[str] = Field(alias="npery", default=None,)


