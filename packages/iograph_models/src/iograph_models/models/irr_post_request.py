from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IrrPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)
	guess: Optional[str] = Field(default=None,alias="guess",)


