from __future__ import annotations
from enum import Enum


class SecurityIntelligenceProfileKind(Enum):
	actor = "actor"
	tool = "tool"
	unknownFutureValue = "unknownFutureValue"

