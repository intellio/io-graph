from __future__ import annotations
from enum import StrEnum


class BrowserSyncSetting(StrEnum):
	notConfigured = "notConfigured"
	blockedWithUserOverride = "blockedWithUserOverride"
	blocked = "blocked"

