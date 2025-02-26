from __future__ import annotations
from enum import Enum


class BrowserSharedCookieStatus(Enum):
	published = "published"
	pendingAdd = "pendingAdd"
	pendingEdit = "pendingEdit"
	pendingDelete = "pendingDelete"
	unknownFutureValue = "unknownFutureValue"

