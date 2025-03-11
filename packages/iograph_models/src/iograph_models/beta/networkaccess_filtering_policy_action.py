from __future__ import annotations
from enum import StrEnum


class NetworkaccessFilteringPolicyAction(StrEnum):
	block = "block"
	allow = "allow"
	unknownFutureValue = "unknownFutureValue"
	bypass = "bypass"
	alert = "alert"

