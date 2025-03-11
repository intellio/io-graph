from __future__ import annotations
from enum import StrEnum


class ConfigurationUsage(StrEnum):
	blocked = "blocked"
	required = "required"
	allowed = "allowed"
	notConfigured = "notConfigured"

