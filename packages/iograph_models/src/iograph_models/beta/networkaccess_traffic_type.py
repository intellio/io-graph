from __future__ import annotations
from enum import StrEnum


class NetworkaccessTrafficType(StrEnum):
	internet = "internet"
	private = "private"
	microsoft365 = "microsoft365"
	all = "all"
	unknownFutureValue = "unknownFutureValue"

