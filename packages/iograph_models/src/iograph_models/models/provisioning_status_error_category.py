from __future__ import annotations
from enum import Enum


class ProvisioningStatusErrorCategory(Enum):
	failure = "failure"
	nonServiceFailure = "nonServiceFailure"
	success = "success"
	unknownFutureValue = "unknownFutureValue"

