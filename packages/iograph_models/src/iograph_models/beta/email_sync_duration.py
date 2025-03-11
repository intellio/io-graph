from __future__ import annotations
from enum import StrEnum


class EmailSyncDuration(StrEnum):
	userDefined = "userDefined"
	oneDay = "oneDay"
	threeDays = "threeDays"
	oneWeek = "oneWeek"
	twoWeeks = "twoWeeks"
	oneMonth = "oneMonth"
	unlimited = "unlimited"

