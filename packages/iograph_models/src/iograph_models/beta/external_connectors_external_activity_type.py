from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsExternalActivityType(StrEnum):
	viewed = "viewed"
	modified = "modified"
	created = "created"
	commented = "commented"
	unknownFutureValue = "unknownFutureValue"

