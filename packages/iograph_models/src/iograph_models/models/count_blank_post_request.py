from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Count_blankPostRequest(BaseModel):
	range: Optional[str] = Field(default=None,alias="range",)


