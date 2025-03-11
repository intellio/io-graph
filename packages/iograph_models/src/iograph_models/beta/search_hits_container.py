from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchHitsContainer(BaseModel):
	aggregations: Optional[list[SearchAggregation]] = Field(alias="aggregations",default=None,)
	hits: Optional[list[SearchHit]] = Field(alias="hits",default=None,)
	moreResultsAvailable: Optional[bool] = Field(alias="moreResultsAvailable",default=None,)
	total: Optional[int] = Field(alias="total",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .search_aggregation import SearchAggregation
from .search_hit import SearchHit

