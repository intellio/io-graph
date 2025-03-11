from __future__ import annotations
from enum import StrEnum


class AdminConsentState(StrEnum):
	notConfigured = "notConfigured"
	granted = "granted"
	notGranted = "notGranted"

