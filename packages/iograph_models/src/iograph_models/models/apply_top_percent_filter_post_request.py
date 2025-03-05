from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Apply_top_percent_filterPostRequest(BaseModel):
	percent: Optional[int] = Field(default=None,alias="percent",)


