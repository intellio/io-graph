from __future__ import annotations
from enum import Enum


class AccessPackageCatalogType(Enum):
	userManaged = "userManaged"
	serviceDefault = "serviceDefault"
	serviceManaged = "serviceManaged"
	unknownFutureValue = "unknownFutureValue"

