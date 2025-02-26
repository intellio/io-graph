from __future__ import annotations
from enum import Enum


class PrintOrientation(Enum):
	portrait = "portrait"
	landscape = "landscape"
	reverseLandscape = "reverseLandscape"
	reversePortrait = "reversePortrait"
	unknownFutureValue = "unknownFutureValue"

