from __future__ import annotations
from enum import Enum


class Win32LobAppRegistryRuleOperationType(Enum):
	notConfigured = "notConfigured"
	exists = "exists"
	doesNotExist = "doesNotExist"
	string = "string"
	integer = "integer"
	version = "version"

