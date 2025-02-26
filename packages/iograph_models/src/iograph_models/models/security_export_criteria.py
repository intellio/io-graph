from __future__ import annotations
from enum import Enum


class SecurityExportCriteria(Enum):
	searchHits = "searchHits"
	partiallyIndexed = "partiallyIndexed"
	unknownFutureValue = "unknownFutureValue"

