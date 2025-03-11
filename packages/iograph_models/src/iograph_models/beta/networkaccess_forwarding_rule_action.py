from __future__ import annotations
from enum import StrEnum


class NetworkaccessForwardingRuleAction(StrEnum):
	bypass = "bypass"
	forward = "forward"
	unknownFutureValue = "unknownFutureValue"

