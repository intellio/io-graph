from __future__ import annotations
from enum import StrEnum


class RecurrencePatternType(StrEnum):
	daily = "daily"
	weekly = "weekly"
	absoluteMonthly = "absoluteMonthly"
	relativeMonthly = "relativeMonthly"
	absoluteYearly = "absoluteYearly"
	relativeYearly = "relativeYearly"

