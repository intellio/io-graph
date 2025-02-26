from __future__ import annotations
from enum import Enum


class RecurrencePatternType(Enum):
	daily = "daily"
	weekly = "weekly"
	absoluteMonthly = "absoluteMonthly"
	relativeMonthly = "relativeMonthly"
	absoluteYearly = "absoluteYearly"
	relativeYearly = "relativeYearly"

