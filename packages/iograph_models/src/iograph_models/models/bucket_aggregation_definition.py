from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BucketAggregationDefinition(BaseModel):
	isDescending: Optional[bool] = Field(default=None,alias="isDescending",)
	minimumCount: Optional[int] = Field(default=None,alias="minimumCount",)
	prefixFilter: Optional[str] = Field(default=None,alias="prefixFilter",)
	ranges: Optional[list[BucketAggregationRange]] = Field(default=None,alias="ranges",)
	sortBy: Optional[BucketAggregationSortProperty] = Field(default=None,alias="sortBy",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .bucket_aggregation_range import BucketAggregationRange
from .bucket_aggregation_sort_property import BucketAggregationSortProperty

