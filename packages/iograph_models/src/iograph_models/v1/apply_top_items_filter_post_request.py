from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Apply_top_items_filterPostRequest(BaseModel):
	count: Optional[int] = Field(alias="count", default=None,)

