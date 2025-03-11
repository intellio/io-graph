from __future__ import annotations
from enum import StrEnum


class BucketAggregationSortProperty(StrEnum):
	count = "count"
	keyAsString = "keyAsString"
	keyAsNumber = "keyAsNumber"
	unknownFutureValue = "unknownFutureValue"

