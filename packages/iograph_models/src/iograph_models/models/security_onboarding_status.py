from __future__ import annotations
from enum import Enum


class SecurityOnboardingStatus(Enum):
	insufficientInfo = "insufficientInfo"
	onboarded = "onboarded"
	canBeOnboarded = "canBeOnboarded"
	unsupported = "unsupported"
	unknownFutureValue = "unknownFutureValue"

