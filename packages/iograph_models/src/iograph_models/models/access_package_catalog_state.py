from __future__ import annotations
from enum import Enum


class AccessPackageCatalogState(Enum):
	unpublished = "unpublished"
	published = "published"
	unknownFutureValue = "unknownFutureValue"

