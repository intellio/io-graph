from __future__ import annotations
from enum import StrEnum


class NetworkaccessTlsAction(StrEnum):
	bypassed = "bypassed"
	intercepted = "intercepted"
	unknownFutureValue = "unknownFutureValue"

