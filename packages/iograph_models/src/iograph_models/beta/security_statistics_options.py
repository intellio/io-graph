from __future__ import annotations
from enum import StrEnum


class SecurityStatisticsOptions(StrEnum):
	includeRefiners = "includeRefiners"
	includeQueryStats = "includeQueryStats"
	includeUnindexedStats = "includeUnindexedStats"
	advancedIndexing = "advancedIndexing"
	locationsWithoutHits = "locationsWithoutHits"
	unknownFutureValue = "unknownFutureValue"

