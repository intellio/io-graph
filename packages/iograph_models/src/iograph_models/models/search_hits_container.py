from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchHitsContainer(BaseModel):
	aggregations: Optional[list[SearchAggregation]] = Field(default=None,alias="aggregations",)
	hits: Optional[list[SearchHit]] = Field(default=None,alias="hits",)
	moreResultsAvailable: Optional[bool] = Field(default=None,alias="moreResultsAvailable",)
	total: Optional[int] = Field(default=None,alias="total",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .search_aggregation import SearchAggregation
from .search_hit import SearchHit

