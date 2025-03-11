from __future__ import annotations
from enum import StrEnum


class SiteArchiveStatus(StrEnum):
	recentlyArchived = "recentlyArchived"
	fullyArchived = "fullyArchived"
	reactivating = "reactivating"
	unknownFutureValue = "unknownFutureValue"

