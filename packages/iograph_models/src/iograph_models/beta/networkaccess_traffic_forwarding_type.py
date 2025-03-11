from __future__ import annotations
from enum import StrEnum


class NetworkaccessTrafficForwardingType(StrEnum):
	m365 = "m365"
	internet = "internet"
	private = "private"
	unknownFutureValue = "unknownFutureValue"

