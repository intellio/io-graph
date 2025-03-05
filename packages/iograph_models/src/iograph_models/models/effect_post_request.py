from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EffectPostRequest(BaseModel):
	nominalRate: Optional[str] = Field(default=None,alias="nominalRate",)
	npery: Optional[str] = Field(default=None,alias="npery",)


