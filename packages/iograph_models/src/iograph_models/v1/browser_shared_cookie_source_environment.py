from __future__ import annotations
from enum import StrEnum


class BrowserSharedCookieSourceEnvironment(StrEnum):
	microsoftEdge = "microsoftEdge"
	internetExplorer11 = "internetExplorer11"
	both = "both"
	unknownFutureValue = "unknownFutureValue"

