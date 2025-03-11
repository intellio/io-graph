from __future__ import annotations
from enum import StrEnum


class Win32LobAppRuleOperator(StrEnum):
	notConfigured = "notConfigured"
	equal = "equal"
	notEqual = "notEqual"
	greaterThan = "greaterThan"
	greaterThanOrEqual = "greaterThanOrEqual"
	lessThan = "lessThan"
	lessThanOrEqual = "lessThanOrEqual"

