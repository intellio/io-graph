from __future__ import annotations
from enum import StrEnum


class VpnOnDemandRuleConnectionAction(StrEnum):
	connect = "connect"
	evaluateConnection = "evaluateConnection"
	ignore = "ignore"
	disconnect = "disconnect"

