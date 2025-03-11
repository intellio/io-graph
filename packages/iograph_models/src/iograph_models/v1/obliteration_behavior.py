from __future__ import annotations
from enum import StrEnum


class ObliterationBehavior(StrEnum):
	default = "default"
	doNotObliterate = "doNotObliterate"
	obliterateWithWarning = "obliterateWithWarning"
	always = "always"
	unknownFutureValue = "unknownFutureValue"

