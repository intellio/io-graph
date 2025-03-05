from __future__ import annotations
from enum import StrEnum


class SecurityExportCriteria(StrEnum):
	searchHits = "searchHits"
	partiallyIndexed = "partiallyIndexed"
	unknownFutureValue = "unknownFutureValue"

