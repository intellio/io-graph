from __future__ import annotations
from enum import StrEnum


class MacOSGatekeeperAppSources(StrEnum):
	notConfigured = "notConfigured"
	macAppStore = "macAppStore"
	macAppStoreAndIdentifiedDevelopers = "macAppStoreAndIdentifiedDevelopers"
	anywhere = "anywhere"

