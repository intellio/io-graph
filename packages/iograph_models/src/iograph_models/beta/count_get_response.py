from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CountGetResponse(BaseModel):
	value: Optional[int] = Field(alias="value", default=None,)

