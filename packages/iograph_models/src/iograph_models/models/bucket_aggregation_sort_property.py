from __future__ import annotations
from enum import Enum


class BucketAggregationSortProperty(Enum):
	count = "count"
	keyAsString = "keyAsString"
	keyAsNumber = "keyAsNumber"
	unknownFutureValue = "unknownFutureValue"

