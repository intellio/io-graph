from __future__ import annotations
from enum import StrEnum


class WelcomeScreenMeetingInformation(StrEnum):
	userDefined = "userDefined"
	showOrganizerAndTimeOnly = "showOrganizerAndTimeOnly"
	showOrganizerAndTimeAndSubject = "showOrganizerAndTimeAndSubject"

