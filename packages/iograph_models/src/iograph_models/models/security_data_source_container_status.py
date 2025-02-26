from __future__ import annotations
from enum import Enum


class SecurityDataSourceContainerStatus(Enum):
	active = "active"
	released = "released"
	unknownFutureValue = "unknownFutureValue"

