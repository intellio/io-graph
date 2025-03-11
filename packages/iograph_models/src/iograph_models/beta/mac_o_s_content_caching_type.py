from __future__ import annotations
from enum import StrEnum


class MacOSContentCachingType(StrEnum):
	notConfigured = "notConfigured"
	userContentOnly = "userContentOnly"
	sharedContentOnly = "sharedContentOnly"

