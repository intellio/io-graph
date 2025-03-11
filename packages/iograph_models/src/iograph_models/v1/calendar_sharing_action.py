from __future__ import annotations
from enum import StrEnum


class CalendarSharingAction(StrEnum):
	accept = "accept"
	acceptAndViewCalendar = "acceptAndViewCalendar"
	viewCalendar = "viewCalendar"
	addThisCalendar = "addThisCalendar"

