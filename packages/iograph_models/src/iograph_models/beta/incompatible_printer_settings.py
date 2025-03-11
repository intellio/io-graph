from __future__ import annotations
from enum import StrEnum


class IncompatiblePrinterSettings(StrEnum):
	show = "show"
	hide = "hide"
	unknownFutureValue = "unknownFutureValue"

