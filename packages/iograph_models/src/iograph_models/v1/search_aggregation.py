from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchAggregation(BaseModel):
	buckets: Optional[list[SearchBucket]] = Field(alias="buckets", default=None,)
	field: Optional[str] = Field(alias="field", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .search_bucket import SearchBucket

