from __future__ import annotations
from enum import StrEnum


class ServiceHealthClassificationType(StrEnum):
	advisory = "advisory"
	incident = "incident"
	unknownFutureValue = "unknownFutureValue"

