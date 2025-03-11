from __future__ import annotations
from enum import StrEnum


class DefenderSubmitSamplesConsentType(StrEnum):
	sendSafeSamplesAutomatically = "sendSafeSamplesAutomatically"
	alwaysPrompt = "alwaysPrompt"
	neverSend = "neverSend"
	sendAllSamplesAutomatically = "sendAllSamplesAutomatically"

