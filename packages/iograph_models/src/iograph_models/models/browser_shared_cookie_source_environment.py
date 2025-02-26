from __future__ import annotations
from enum import Enum


class BrowserSharedCookieSourceEnvironment(Enum):
	microsoftEdge = "microsoftEdge"
	internetExplorer11 = "internetExplorer11"
	both = "both"
	unknownFutureValue = "unknownFutureValue"

