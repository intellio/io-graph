from __future__ import annotations
from enum import StrEnum


class WindowsUpdateForBusinessUpdateWeeks(StrEnum):
	userDefined = "userDefined"
	firstWeek = "firstWeek"
	secondWeek = "secondWeek"
	thirdWeek = "thirdWeek"
	fourthWeek = "fourthWeek"
	everyWeek = "everyWeek"
	unknownFutureValue = "unknownFutureValue"

