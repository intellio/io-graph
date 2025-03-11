from __future__ import annotations
from enum import StrEnum


class WebBrowserCookieSettings(StrEnum):
	browserDefault = "browserDefault"
	blockAlways = "blockAlways"
	allowCurrentWebSite = "allowCurrentWebSite"
	allowFromWebsitesVisited = "allowFromWebsitesVisited"
	allowAlways = "allowAlways"

