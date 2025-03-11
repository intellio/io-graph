from __future__ import annotations
from enum import StrEnum


class BrowserSiteTargetEnvironment(StrEnum):
	internetExplorerMode = "internetExplorerMode"
	internetExplorer11 = "internetExplorer11"
	microsoftEdge = "microsoftEdge"
	configurable = "configurable"
	none = "none"
	unknownFutureValue = "unknownFutureValue"

