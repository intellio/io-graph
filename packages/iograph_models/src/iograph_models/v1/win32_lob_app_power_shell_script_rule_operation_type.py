from __future__ import annotations
from enum import StrEnum


class Win32LobAppPowerShellScriptRuleOperationType(StrEnum):
	notConfigured = "notConfigured"
	string = "string"
	dateTime = "dateTime"
	integer = "integer"
	float = "float"
	version = "version"
	boolean = "boolean"

