from __future__ import annotations
from enum import StrEnum


class ApproverRole(StrEnum):
	owner = "owner"
	approver = "approver"
	unknownFutureValue = "unknownFutureValue"

