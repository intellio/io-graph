from __future__ import annotations
from enum import Enum


class PromptLoginBehavior(Enum):
	translateToFreshPasswordAuthentication = "translateToFreshPasswordAuthentication"
	nativeSupport = "nativeSupport"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

