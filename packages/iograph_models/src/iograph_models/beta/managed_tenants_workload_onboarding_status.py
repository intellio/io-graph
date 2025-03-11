from __future__ import annotations
from enum import StrEnum


class ManagedTenantsWorkloadOnboardingStatus(StrEnum):
	notOnboarded = "notOnboarded"
	onboarded = "onboarded"
	unknownFutureValue = "unknownFutureValue"

