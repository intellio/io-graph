from __future__ import annotations
from enum import StrEnum


class ProvisionState(StrEnum):
	notProvisioned = "notProvisioned"
	provisioningInProgress = "provisioningInProgress"
	provisioningFailed = "provisioningFailed"
	provisioningCompleted = "provisioningCompleted"
	unknownFutureValue = "unknownFutureValue"

