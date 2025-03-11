from __future__ import annotations
from enum import StrEnum


class ManagedTenantsTenantOnboardingStatus(StrEnum):
	ineligible = "ineligible"
	inProcess = "inProcess"
	active = "active"
	inactive = "inactive"
	unknownFutureValue = "unknownFutureValue"
	disabled = "disabled"

