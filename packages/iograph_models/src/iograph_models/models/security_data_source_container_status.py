from __future__ import annotations
from enum import StrEnum


class SecurityDataSourceContainerStatus(StrEnum):
	active = "active"
	released = "released"
	unknownFutureValue = "unknownFutureValue"

