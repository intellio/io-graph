from __future__ import annotations
from enum import StrEnum


class MacOSSystemExtensionType(StrEnum):
	driverExtensionsAllowed = "driverExtensionsAllowed"
	networkExtensionsAllowed = "networkExtensionsAllowed"
	endpointSecurityExtensionsAllowed = "endpointSecurityExtensionsAllowed"

