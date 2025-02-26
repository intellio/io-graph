from __future__ import annotations
from enum import Enum


class SiteArchiveStatus(Enum):
	recentlyArchived = "recentlyArchived"
	fullyArchived = "fullyArchived"
	reactivating = "reactivating"
	unknownFutureValue = "unknownFutureValue"

