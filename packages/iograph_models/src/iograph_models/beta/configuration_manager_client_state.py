from __future__ import annotations
from enum import StrEnum


class ConfigurationManagerClientState(StrEnum):
	unknown = "unknown"
	installed = "installed"
	healthy = "healthy"
	installFailed = "installFailed"
	updateFailed = "updateFailed"
	communicationError = "communicationError"

