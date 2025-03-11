from __future__ import annotations
from enum import StrEnum


class PartnerSecuritySecurityRequirementType(StrEnum):
	mfaEnforcedForAdmins = "mfaEnforcedForAdmins"
	mfaEnforcedForAdminsOfCustomers = "mfaEnforcedForAdminsOfCustomers"
	securityAlertsPromptlyResolved = "securityAlertsPromptlyResolved"
	securityContactProvided = "securityContactProvided"
	spendingBudgetSetForCustomerAzureSubscriptions = "spendingBudgetSetForCustomerAzureSubscriptions"
	unknownFutureValue = "unknownFutureValue"

