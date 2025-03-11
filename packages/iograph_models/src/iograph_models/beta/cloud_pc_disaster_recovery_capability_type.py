from __future__ import annotations
from enum import StrEnum


class CloudPcDisasterRecoveryCapabilityType(StrEnum):
	none = "none"
	failover = "failover"
	failback = "failback"
	unknownFutureValue = "unknownFutureValue"

