from __future__ import annotations
from enum import Enum


class ImageTaggingChoice(Enum):
	disabled = "disabled"
	basic = "basic"
	enhanced = "enhanced"
	unknownFutureValue = "unknownFutureValue"

