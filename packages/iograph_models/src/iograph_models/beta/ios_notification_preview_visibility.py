from __future__ import annotations
from enum import StrEnum


class IosNotificationPreviewVisibility(StrEnum):
	notConfigured = "notConfigured"
	alwaysShow = "alwaysShow"
	hideWhenLocked = "hideWhenLocked"
	neverShow = "neverShow"

