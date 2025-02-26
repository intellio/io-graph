from __future__ import annotations
from enum import Enum


class DefenderPromptForSampleSubmission(Enum):
	userDefined = "userDefined"
	alwaysPrompt = "alwaysPrompt"
	promptBeforeSendingPersonalData = "promptBeforeSendingPersonalData"
	neverSendData = "neverSendData"
	sendAllDataWithoutPrompting = "sendAllDataWithoutPrompting"

