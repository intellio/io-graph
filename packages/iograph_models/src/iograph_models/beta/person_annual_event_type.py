from __future__ import annotations
from enum import StrEnum


class PersonAnnualEventType(StrEnum):
	birthday = "birthday"
	wedding = "wedding"
	work = "work"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

