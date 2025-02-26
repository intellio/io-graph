from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchAggregation(BaseModel):
	buckets: list[SearchBucket] = Field(alias="buckets",)
	field: Optional[str] = Field(default=None,alias="field",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_bucket import SearchBucket

