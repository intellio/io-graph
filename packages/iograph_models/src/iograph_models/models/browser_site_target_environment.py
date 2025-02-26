from __future__ import annotations
from enum import Enum


class BrowserSiteTargetEnvironment(Enum):
	internetExplorerMode = "internetExplorerMode"
	internetExplorer11 = "internetExplorer11"
	microsoftEdge = "microsoftEdge"
	configurable = "configurable"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

