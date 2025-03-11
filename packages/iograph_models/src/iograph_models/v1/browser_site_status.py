from __future__ import annotations
from enum import StrEnum


class BrowserSiteStatus(StrEnum):
	published = "published"
	pendingAdd = "pendingAdd"
	pendingEdit = "pendingEdit"
	pendingDelete = "pendingDelete"
	unknownFutureValue = "unknownFutureValue"

