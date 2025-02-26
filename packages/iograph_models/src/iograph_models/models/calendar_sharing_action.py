from __future__ import annotations
from enum import Enum


class CalendarSharingAction(Enum):
	accept = "accept"
	acceptAndViewCalendar = "acceptAndViewCalendar"
	viewCalendar = "viewCalendar"
	addThisCalendar = "addThisCalendar"

