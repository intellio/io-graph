from __future__ import annotations
from enum import StrEnum


class ConditionalAccessClientApp(StrEnum):
	all = "all"
	browser = "browser"
	mobileAppsAndDesktopClients = "mobileAppsAndDesktopClients"
	exchangeActiveSync = "exchangeActiveSync"
	easSupported = "easSupported"
	other = "other"
	unknownFutureValue = "unknownFutureValue"

