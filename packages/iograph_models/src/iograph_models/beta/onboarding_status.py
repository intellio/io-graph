from __future__ import annotations
from enum import StrEnum


class OnboardingStatus(StrEnum):
	unknown = "unknown"
	inprogress = "inprogress"
	onboarded = "onboarded"
	failed = "failed"
	offboarding = "offboarding"
	unknownFutureValue = "unknownFutureValue"

