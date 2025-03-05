from __future__ import annotations
from enum import StrEnum


class AccessPackageCatalogType(StrEnum):
	userManaged = "userManaged"
	serviceDefault = "serviceDefault"
	serviceManaged = "serviceManaged"
	unknownFutureValue = "unknownFutureValue"

