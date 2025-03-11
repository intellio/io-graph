from __future__ import annotations
from enum import StrEnum


class BitLockerRecoveryPasswordRotationType(StrEnum):
	notConfigured = "notConfigured"
	disabled = "disabled"
	enabledForAzureAd = "enabledForAzureAd"
	enabledForAzureAdAndHybrid = "enabledForAzureAdAndHybrid"

