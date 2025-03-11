from __future__ import annotations
from enum import StrEnum


class RiskDetail(StrEnum):
	none = "none"
	adminGeneratedTemporaryPassword = "adminGeneratedTemporaryPassword"
	userPerformedSecuredPasswordChange = "userPerformedSecuredPasswordChange"
	userPerformedSecuredPasswordReset = "userPerformedSecuredPasswordReset"
	adminConfirmedSigninSafe = "adminConfirmedSigninSafe"
	aiConfirmedSigninSafe = "aiConfirmedSigninSafe"
	userPassedMFADrivenByRiskBasedPolicy = "userPassedMFADrivenByRiskBasedPolicy"
	adminDismissedAllRiskForUser = "adminDismissedAllRiskForUser"
	adminConfirmedSigninCompromised = "adminConfirmedSigninCompromised"
	hidden = "hidden"
	adminConfirmedUserCompromised = "adminConfirmedUserCompromised"
	unknownFutureValue = "unknownFutureValue"
	adminConfirmedServicePrincipalCompromised = "adminConfirmedServicePrincipalCompromised"
	adminDismissedAllRiskForServicePrincipal = "adminDismissedAllRiskForServicePrincipal"
	m365DAdminDismissedDetection = "m365DAdminDismissedDetection"
	userChangedPasswordOnPremises = "userChangedPasswordOnPremises"
	adminDismissedRiskForSignIn = "adminDismissedRiskForSignIn"
	adminConfirmedAccountSafe = "adminConfirmedAccountSafe"

