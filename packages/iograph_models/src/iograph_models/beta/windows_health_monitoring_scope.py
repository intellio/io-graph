from __future__ import annotations
from enum import StrEnum


class WindowsHealthMonitoringScope(StrEnum):
	undefined = "undefined"
	healthMonitoring = "healthMonitoring"
	bootPerformance = "bootPerformance"
	windowsUpdates = "windowsUpdates"
	privilegeManagement = "privilegeManagement"

