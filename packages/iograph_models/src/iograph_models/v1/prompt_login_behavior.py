from __future__ import annotations
from enum import StrEnum


class PromptLoginBehavior(StrEnum):
	translateToFreshPasswordAuthentication = "translateToFreshPasswordAuthentication"
	nativeSupport = "nativeSupport"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

