from __future__ import annotations
from enum import StrEnum


class DefenderPromptForSampleSubmission(StrEnum):
	userDefined = "userDefined"
	alwaysPrompt = "alwaysPrompt"
	promptBeforeSendingPersonalData = "promptBeforeSendingPersonalData"
	neverSendData = "neverSendData"
	sendAllDataWithoutPrompting = "sendAllDataWithoutPrompting"

