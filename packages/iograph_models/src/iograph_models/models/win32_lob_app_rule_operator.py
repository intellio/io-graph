from __future__ import annotations
from enum import Enum


class Win32LobAppRuleOperator(Enum):
	notConfigured = "notConfigured"
	equal = "equal"
	notEqual = "notEqual"
	greaterThan = "greaterThan"
	greaterThanOrEqual = "greaterThanOrEqual"
	lessThan = "lessThan"
	lessThanOrEqual = "lessThanOrEqual"

