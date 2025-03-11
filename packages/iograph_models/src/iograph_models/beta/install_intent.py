from __future__ import annotations
from enum import StrEnum


class InstallIntent(StrEnum):
	available = "available"
	required = "required"
	uninstall = "uninstall"
	availableWithoutEnrollment = "availableWithoutEnrollment"

