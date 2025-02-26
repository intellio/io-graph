from __future__ import annotations
from enum import Enum


class BrowserSiteCompatibilityMode(Enum):
	default = "default"
	internetExplorer8Enterprise = "internetExplorer8Enterprise"
	internetExplorer7Enterprise = "internetExplorer7Enterprise"
	internetExplorer11 = "internetExplorer11"
	internetExplorer10 = "internetExplorer10"
	internetExplorer9 = "internetExplorer9"
	internetExplorer8 = "internetExplorer8"
	internetExplorer7 = "internetExplorer7"
	internetExplorer5 = "internetExplorer5"
	unknownFutureValue = "unknownFutureValue"

