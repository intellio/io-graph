from __future__ import annotations
from enum import StrEnum


class MacAddressRandomizationMode(StrEnum):
	automatic = "automatic"
	hardware = "hardware"
	unknownFutureValue = "unknownFutureValue"

