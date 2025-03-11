from __future__ import annotations
from enum import StrEnum


class RootDomains(StrEnum):
	none = "none"
	all = "all"
	allFederated = "allFederated"
	allManaged = "allManaged"
	enumerated = "enumerated"
	allManagedAndEnumeratedFederated = "allManagedAndEnumeratedFederated"
	unknownFutureValue = "unknownFutureValue"

