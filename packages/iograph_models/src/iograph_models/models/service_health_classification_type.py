from __future__ import annotations
from enum import Enum


class ServiceHealthClassificationType(Enum):
	advisory = "advisory"
	incident = "incident"
	unknownFutureValue = "unknownFutureValue"

