from __future__ import annotations
from enum import StrEnum


class AiInteractionType(StrEnum):
	userPrompt = "userPrompt"
	aiResponse = "aiResponse"
	unknownFutureValue = "unknownFutureValue"

