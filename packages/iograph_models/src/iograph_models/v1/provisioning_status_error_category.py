from __future__ import annotations
from enum import StrEnum


class ProvisioningStatusErrorCategory(StrEnum):
	failure = "failure"
	nonServiceFailure = "nonServiceFailure"
	success = "success"
	unknownFutureValue = "unknownFutureValue"

