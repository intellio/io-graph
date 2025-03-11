from __future__ import annotations
from enum import StrEnum


class AppLockerApplicationControlType(StrEnum):
	notConfigured = "notConfigured"
	enforceComponentsAndStoreApps = "enforceComponentsAndStoreApps"
	auditComponentsAndStoreApps = "auditComponentsAndStoreApps"
	enforceComponentsStoreAppsAndSmartlocker = "enforceComponentsStoreAppsAndSmartlocker"
	auditComponentsStoreAppsAndSmartlocker = "auditComponentsStoreAppsAndSmartlocker"

