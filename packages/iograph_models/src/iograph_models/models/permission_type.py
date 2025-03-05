from __future__ import annotations
from enum import StrEnum


class PermissionType(StrEnum):
	delegatedUserConsentable = "delegatedUserConsentable"
	delegated = "delegated"
	application = "application"

