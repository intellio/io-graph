from __future__ import annotations
from enum import StrEnum


class ExternalConnectorsRuleOperation(StrEnum):
	null = "null"
	equals = "equals"
	notEquals = "notEquals"
	contains = "contains"
	notContains = "notContains"
	lessThan = "lessThan"
	greaterThan = "greaterThan"
	startsWith = "startsWith"
	unknownFutureValue = "unknownFutureValue"

