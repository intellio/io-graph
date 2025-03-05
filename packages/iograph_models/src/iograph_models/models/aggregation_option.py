from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AggregationOption(BaseModel):
	bucketDefinition: Optional[BucketAggregationDefinition] = Field(default=None,alias="bucketDefinition",)
	field: Optional[str] = Field(default=None,alias="field",)
	size: Optional[int] = Field(default=None,alias="size",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .bucket_aggregation_definition import BucketAggregationDefinition

