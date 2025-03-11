from __future__ import annotations
from enum import StrEnum


class BrowserSiteListStatus(StrEnum):
	draft = "draft"
	published = "published"
	pending = "pending"
	unknownFutureValue = "unknownFutureValue"

