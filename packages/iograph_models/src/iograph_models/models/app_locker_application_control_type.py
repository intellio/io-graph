from __future__ import annotations
from enum import Enum


class AppLockerApplicationControlType(Enum):
	notConfigured = "notConfigured"
	enforceComponentsAndStoreApps = "enforceComponentsAndStoreApps"
	auditComponentsAndStoreApps = "auditComponentsAndStoreApps"
	enforceComponentsStoreAppsAndSmartlocker = "enforceComponentsStoreAppsAndSmartlocker"
	auditComponentsStoreAppsAndSmartlocker = "auditComponentsStoreAppsAndSmartlocker"

