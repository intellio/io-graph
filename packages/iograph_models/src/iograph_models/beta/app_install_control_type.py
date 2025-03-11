from __future__ import annotations
from enum import StrEnum


class AppInstallControlType(StrEnum):
	notConfigured = "notConfigured"
	anywhere = "anywhere"
	storeOnly = "storeOnly"
	recommendations = "recommendations"
	preferStore = "preferStore"

