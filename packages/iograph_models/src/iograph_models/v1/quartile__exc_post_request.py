from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Quartile__excPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)
	quart: Optional[str] = Field(alias="quart", default=None,)


