from __future__ import annotations
from enum import StrEnum


class Operator(StrEnum):
	none = "none"
	and_ = "and_"
	or_ = "or_"
	isEquals = "isEquals"
	notEquals = "notEquals"
	greaterThan = "greaterThan"
	lessThan = "lessThan"
	between = "between"
	notBetween = "notBetween"
	greaterEquals = "greaterEquals"
	lessEquals = "lessEquals"
	dayTimeBetween = "dayTimeBetween"
	beginsWith = "beginsWith"
	notBeginsWith = "notBeginsWith"
	endsWith = "endsWith"
	notEndsWith = "notEndsWith"
	contains = "contains"
	notContains = "notContains"
	allOf = "allOf"
	oneOf = "oneOf"
	noneOf = "noneOf"
	setEquals = "setEquals"
	orderedSetEquals = "orderedSetEquals"
	subsetOf = "subsetOf"
	excludesAll = "excludesAll"

