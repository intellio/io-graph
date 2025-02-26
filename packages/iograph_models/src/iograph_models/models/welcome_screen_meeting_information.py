from __future__ import annotations
from enum import Enum


class WelcomeScreenMeetingInformation(Enum):
	userDefined = "userDefined"
	showOrganizerAndTimeOnly = "showOrganizerAndTimeOnly"
	showOrganizerAndTimeAndSubject = "showOrganizerAndTimeAndSubject"

