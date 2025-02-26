from __future__ import annotations
from enum import Enum


class OnlineMeetingPresenters(Enum):
	everyone = "everyone"
	organization = "organization"
	roleIsPresenter = "roleIsPresenter"
	organizer = "organizer"
	unknownFutureValue = "unknownFutureValue"

