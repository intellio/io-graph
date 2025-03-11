from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerAppAutoUpdatePolicyType(StrEnum):
	notConfigured = "notConfigured"
	userChoice = "userChoice"
	never = "never"
	wiFiOnly = "wiFiOnly"
	always = "always"

