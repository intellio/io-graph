from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Apply_top_percent_filterPostRequest(BaseModel):
	percent: Optional[int] = Field(alias="percent", default=None,)

