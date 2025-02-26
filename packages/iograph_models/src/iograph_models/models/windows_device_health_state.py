from __future__ import annotations
from enum import Enum


class WindowsDeviceHealthState(Enum):
	clean = "clean"
	fullScanPending = "fullScanPending"
	rebootPending = "rebootPending"
	manualStepsPending = "manualStepsPending"
	offlineScanPending = "offlineScanPending"
	critical = "critical"

