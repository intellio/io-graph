from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsStandardUserElevationPromptBehaviorType(StrEnum):
	notConfigured = "notConfigured"
	automaticallyDenyElevationRequests = "automaticallyDenyElevationRequests"
	promptForCredentialsOnTheSecureDesktop = "promptForCredentialsOnTheSecureDesktop"
	promptForCredentials = "promptForCredentials"

