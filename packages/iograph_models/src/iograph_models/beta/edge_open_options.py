from __future__ import annotations
from enum import StrEnum


class EdgeOpenOptions(StrEnum):
	notConfigured = "notConfigured"
	startPage = "startPage"
	newTabPage = "newTabPage"
	previousPages = "previousPages"
	specificPages = "specificPages"

