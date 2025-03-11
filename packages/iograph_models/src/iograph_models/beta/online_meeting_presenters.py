from __future__ import annotations
from enum import StrEnum


class OnlineMeetingPresenters(StrEnum):
	everyone = "everyone"
	organization = "organization"
	roleIsPresenter = "roleIsPresenter"
	organizer = "organizer"
	unknownFutureValue = "unknownFutureValue"

