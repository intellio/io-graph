from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Rand_betweenPostRequest(BaseModel):
	bottom: Optional[str] = Field(default=None,alias="bottom",)
	top: Optional[str] = Field(default=None,alias="top",)


