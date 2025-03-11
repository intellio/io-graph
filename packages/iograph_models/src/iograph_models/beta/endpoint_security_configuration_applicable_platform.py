from __future__ import annotations
from enum import StrEnum


class EndpointSecurityConfigurationApplicablePlatform(StrEnum):
	unknown = "unknown"
	macOS = "macOS"
	windows10AndLater = "windows10AndLater"
	windows10AndWindowsServer = "windows10AndWindowsServer"

