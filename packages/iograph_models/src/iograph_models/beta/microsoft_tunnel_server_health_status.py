from __future__ import annotations
from enum import StrEnum


class MicrosoftTunnelServerHealthStatus(StrEnum):
	unknown = "unknown"
	healthy = "healthy"
	unhealthy = "unhealthy"
	warning = "warning"
	offline = "offline"
	upgradeInProgress = "upgradeInProgress"
	upgradeFailed = "upgradeFailed"
	unknownFutureValue = "unknownFutureValue"

