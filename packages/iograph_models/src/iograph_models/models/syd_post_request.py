from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SydPostRequest(BaseModel):
	cost: Optional[str] = Field(default=None,alias="cost",)
	salvage: Optional[str] = Field(default=None,alias="salvage",)
	life: Optional[str] = Field(default=None,alias="life",)
	per: Optional[str] = Field(default=None,alias="per",)


