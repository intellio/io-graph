from __future__ import annotations
from enum import StrEnum


class PrintOrientation(StrEnum):
	portrait = "portrait"
	landscape = "landscape"
	reverseLandscape = "reverseLandscape"
	reversePortrait = "reversePortrait"
	unknownFutureValue = "unknownFutureValue"

