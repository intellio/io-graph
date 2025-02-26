from __future__ import annotations
from enum import Enum


class ObliterationBehavior(Enum):
	default = "default"
	doNotObliterate = "doNotObliterate"
	obliterateWithWarning = "obliterateWithWarning"
	always = "always"
	unknownFutureValue = "unknownFutureValue"

