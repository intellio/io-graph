from __future__ import annotations
from enum import StrEnum


class SecurityIntelligenceProfileKind(StrEnum):
	actor = "actor"
	tool = "tool"
	unknownFutureValue = "unknownFutureValue"

