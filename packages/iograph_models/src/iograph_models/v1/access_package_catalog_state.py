from __future__ import annotations
from enum import StrEnum


class AccessPackageCatalogState(StrEnum):
	unpublished = "unpublished"
	published = "published"
	unknownFutureValue = "unknownFutureValue"

