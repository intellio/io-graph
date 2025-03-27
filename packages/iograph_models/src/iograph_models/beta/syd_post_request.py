from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SydPostRequest(BaseModel):
	cost: Optional[str] = Field(alias="cost", default=None,)
	salvage: Optional[str] = Field(alias="salvage", default=None,)
	life: Optional[str] = Field(alias="life", default=None,)
	per: Optional[str] = Field(alias="per", default=None,)


