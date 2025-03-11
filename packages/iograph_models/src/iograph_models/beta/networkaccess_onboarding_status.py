from __future__ import annotations
from enum import StrEnum


class NetworkaccessOnboardingStatus(StrEnum):
	offboarded = "offboarded"
	offboardingInProgress = "offboardingInProgress"
	onboardingInProgress = "onboardingInProgress"
	onboarded = "onboarded"
	onboardingErrorOccurred = "onboardingErrorOccurred"
	offboardingErrorOccurred = "offboardingErrorOccurred"
	unknownFutureValue = "unknownFutureValue"

