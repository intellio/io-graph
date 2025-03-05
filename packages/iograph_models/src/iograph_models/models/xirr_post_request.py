from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class XirrPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)
	dates: Optional[str] = Field(default=None,alias="dates",)
	guess: Optional[str] = Field(default=None,alias="guess",)


