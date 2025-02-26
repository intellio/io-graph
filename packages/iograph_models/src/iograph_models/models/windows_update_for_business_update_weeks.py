from __future__ import annotations
from enum import Enum


class WindowsUpdateForBusinessUpdateWeeks(Enum):
	userDefined = "userDefined"
	firstWeek = "firstWeek"
	secondWeek = "secondWeek"
	thirdWeek = "thirdWeek"
	fourthWeek = "fourthWeek"
	everyWeek = "everyWeek"
	unknownFutureValue = "unknownFutureValue"

