from __future__ import annotations
from enum import Enum


class WebBrowserCookieSettings(Enum):
	browserDefault = "browserDefault"
	blockAlways = "blockAlways"
	allowCurrentWebSite = "allowCurrentWebSite"
	allowFromWebsitesVisited = "allowFromWebsitesVisited"
	allowAlways = "allowAlways"

