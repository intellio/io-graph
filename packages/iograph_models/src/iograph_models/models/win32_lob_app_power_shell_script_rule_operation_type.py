from __future__ import annotations
from enum import Enum


class Win32LobAppPowerShellScriptRuleOperationType(Enum):
	notConfigured = "notConfigured"
	string = "string"
	dateTime = "dateTime"
	integer = "integer"
	float = "float"
	version = "version"
	boolean = "boolean"

