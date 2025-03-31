from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AggregationOption(BaseModel):
	bucketDefinition: Optional[BucketAggregationDefinition] = Field(alias="bucketDefinition", default=None,)
	field: Optional[str] = Field(alias="field", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .bucket_aggregation_definition import BucketAggregationDefinition
