from __future__ import annotations
from enum import StrEnum


class ManagedTenantsWorkloadActionCategory(StrEnum):
	automated = "automated"
	manual = "manual"
	unknownFutureValue = "unknownFutureValue"

