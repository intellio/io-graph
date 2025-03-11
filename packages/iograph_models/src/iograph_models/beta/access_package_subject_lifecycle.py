from __future__ import annotations
from enum import StrEnum


class AccessPackageSubjectLifecycle(StrEnum):
	notDefined = "notDefined"
	notGoverned = "notGoverned"
	governed = "governed"
	unknownFutureValue = "unknownFutureValue"

