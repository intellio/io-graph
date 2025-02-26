from __future__ import annotations
from enum import Enum


class ExternalConnectorsExternalActivityType(Enum):
	viewed = "viewed"
	modified = "modified"
	created = "created"
	commented = "commented"
	unknownFutureValue = "unknownFutureValue"

