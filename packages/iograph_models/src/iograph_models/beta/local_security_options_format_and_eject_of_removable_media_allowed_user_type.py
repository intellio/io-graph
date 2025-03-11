from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType(StrEnum):
	notConfigured = "notConfigured"
	administrators = "administrators"
	administratorsAndPowerUsers = "administratorsAndPowerUsers"
	administratorsAndInteractiveUsers = "administratorsAndInteractiveUsers"

