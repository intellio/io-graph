from __future__ import annotations
from enum import StrEnum


class Win32LobAppRegistryDetectionType(StrEnum):
	notConfigured = "notConfigured"
	exists = "exists"
	doesNotExist = "doesNotExist"
	string = "string"
	integer = "integer"
	version = "version"

