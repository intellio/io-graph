from __future__ import annotations
from enum import StrEnum


class AssignmentFilterOperator(StrEnum):
	notSet = "notSet"
	equals = "equals"
	notEquals = "notEquals"
	startsWith = "startsWith"
	notStartsWith = "notStartsWith"
	contains = "contains"
	notContains = "notContains"
	in_ = "in_"
	notIn = "notIn"
	endsWith = "endsWith"
	notEndsWith = "notEndsWith"
	greaterThan = "greaterThan"
	greaterThanOrEquals = "greaterThanOrEquals"
	lessThan = "lessThan"
	lessThanOrEquals = "lessThanOrEquals"
	unknownFutureValue = "unknownFutureValue"

