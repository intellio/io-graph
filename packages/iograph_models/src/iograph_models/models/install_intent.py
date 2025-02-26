from __future__ import annotations
from enum import Enum


class InstallIntent(Enum):
	available = "available"
	required = "required"
	uninstall = "uninstall"
	availableWithoutEnrollment = "availableWithoutEnrollment"

