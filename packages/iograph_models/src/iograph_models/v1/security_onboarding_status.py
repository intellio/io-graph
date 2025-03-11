from __future__ import annotations
from enum import StrEnum


class SecurityOnboardingStatus(StrEnum):
	insufficientInfo = "insufficientInfo"
	onboarded = "onboarded"
	canBeOnboarded = "canBeOnboarded"
	unsupported = "unsupported"
	unknownFutureValue = "unknownFutureValue"

