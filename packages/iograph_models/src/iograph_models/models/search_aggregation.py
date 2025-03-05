from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchAggregation(BaseModel):
	buckets: Optional[list[SearchBucket]] = Field(default=None,alias="buckets",)
	field: Optional[str] = Field(default=None,alias="field",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_bucket import SearchBucket

