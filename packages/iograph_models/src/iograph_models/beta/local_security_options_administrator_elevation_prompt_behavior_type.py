from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsAdministratorElevationPromptBehaviorType(StrEnum):
	notConfigured = "notConfigured"
	elevateWithoutPrompting = "elevateWithoutPrompting"
	promptForCredentialsOnTheSecureDesktop = "promptForCredentialsOnTheSecureDesktop"
	promptForConsentOnTheSecureDesktop = "promptForConsentOnTheSecureDesktop"
	promptForCredentials = "promptForCredentials"
	promptForConsent = "promptForConsent"
	promptForConsentForNonWindowsBinaries = "promptForConsentForNonWindowsBinaries"

