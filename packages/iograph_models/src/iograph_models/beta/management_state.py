from __future__ import annotations
from enum import StrEnum


class ManagementState(StrEnum):
	managed = "managed"
	retirePending = "retirePending"
	retireFailed = "retireFailed"
	wipePending = "wipePending"
	wipeFailed = "wipeFailed"
	unhealthy = "unhealthy"
	deletePending = "deletePending"
	retireIssued = "retireIssued"
	wipeIssued = "wipeIssued"
	wipeCanceled = "wipeCanceled"
	retireCanceled = "retireCanceled"
	discovered = "discovered"

