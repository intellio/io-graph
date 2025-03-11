from __future__ import annotations
from enum import StrEnum


class MobileAppIntent(StrEnum):
	available = "available"
	notAvailable = "notAvailable"
	requiredInstall = "requiredInstall"
	requiredUninstall = "requiredUninstall"
	requiredAndAvailableInstall = "requiredAndAvailableInstall"
	availableInstallWithoutEnrollment = "availableInstallWithoutEnrollment"
	exclude = "exclude"

