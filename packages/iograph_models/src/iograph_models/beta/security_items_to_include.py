from __future__ import annotations
from enum import StrEnum


class SecurityItemsToInclude(StrEnum):
	searchHits = "searchHits"
	partiallyIndexed = "partiallyIndexed"
	unknownFutureValue = "unknownFutureValue"

