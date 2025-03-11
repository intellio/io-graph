from __future__ import annotations
from enum import StrEnum


class WindowsDeviceHealthState(StrEnum):
	clean = "clean"
	fullScanPending = "fullScanPending"
	rebootPending = "rebootPending"
	manualStepsPending = "manualStepsPending"
	offlineScanPending = "offlineScanPending"
	critical = "critical"

