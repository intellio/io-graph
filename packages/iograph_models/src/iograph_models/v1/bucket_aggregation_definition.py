from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BucketAggregationDefinition(BaseModel):
	isDescending: Optional[bool] = Field(alias="isDescending", default=None,)
	minimumCount: Optional[int] = Field(alias="minimumCount", default=None,)
	prefixFilter: Optional[str] = Field(alias="prefixFilter", default=None,)
	ranges: Optional[list[BucketAggregationRange]] = Field(alias="ranges", default=None,)
	sortBy: Optional[BucketAggregationSortProperty | str] = Field(alias="sortBy", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .bucket_aggregation_range import BucketAggregationRange
from .bucket_aggregation_sort_property import BucketAggregationSortProperty
