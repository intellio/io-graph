from __future__ import annotations
from enum import StrEnum


class DriverApprovalAction(StrEnum):
	approve = "approve"
	decline = "decline"
	suspend = "suspend"

