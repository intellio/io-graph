from __future__ import annotations
from enum import StrEnum


class ImageTaggingChoice(StrEnum):
	disabled = "disabled"
	basic = "basic"
	enhanced = "enhanced"
	unknownFutureValue = "unknownFutureValue"

