from __future__ import annotations
from enum import Enum


class BrowserSiteStatus(Enum):
	published = "published"
	pendingAdd = "pendingAdd"
	pendingEdit = "pendingEdit"
	pendingDelete = "pendingDelete"
	unknownFutureValue = "unknownFutureValue"

