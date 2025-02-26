from __future__ import annotations
from enum import Enum


class BrowserSiteListStatus(Enum):
	draft = "draft"
	published = "published"
	pending = "pending"
	unknownFutureValue = "unknownFutureValue"

