from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsInformationDisplayedOnLockScreenType(StrEnum):
	notConfigured = "notConfigured"
	administrators = "administrators"
	administratorsAndPowerUsers = "administratorsAndPowerUsers"
	administratorsAndInteractiveUsers = "administratorsAndInteractiveUsers"

