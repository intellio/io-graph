from __future__ import annotations
from enum import StrEnum


class PermissionType(StrEnum):
	application = "application"
	delegated = "delegated"
	delegatedUserConsentable = "delegatedUserConsentable"

