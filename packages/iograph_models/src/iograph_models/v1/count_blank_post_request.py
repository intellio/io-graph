from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Count_blankPostRequest(BaseModel):
	range: Optional[str] = Field(alias="range", default=None,)

