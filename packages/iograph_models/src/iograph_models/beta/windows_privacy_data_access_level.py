from __future__ import annotations
from enum import StrEnum


class WindowsPrivacyDataAccessLevel(StrEnum):
	notConfigured = "notConfigured"
	forceAllow = "forceAllow"
	forceDeny = "forceDeny"
	userInControl = "userInControl"

