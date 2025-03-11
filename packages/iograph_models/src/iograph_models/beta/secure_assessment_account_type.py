from __future__ import annotations
from enum import StrEnum


class SecureAssessmentAccountType(StrEnum):
	azureADAccount = "azureADAccount"
	domainAccount = "domainAccount"
	localAccount = "localAccount"
	localGuestAccount = "localGuestAccount"

