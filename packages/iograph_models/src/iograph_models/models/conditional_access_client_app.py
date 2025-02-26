from __future__ import annotations
from enum import Enum


class ConditionalAccessClientApp(Enum):
	all = "all"
	browser = "browser"
	mobileAppsAndDesktopClients = "mobileAppsAndDesktopClients"
	exchangeActiveSync = "exchangeActiveSync"
	easSupported = "easSupported"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

