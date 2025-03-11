from __future__ import annotations
from enum import StrEnum


class MicrosoftEdgeChannel(StrEnum):
	dev = "dev"
	beta = "beta"
	stable = "stable"
	unknownFutureValue = "unknownFutureValue"

