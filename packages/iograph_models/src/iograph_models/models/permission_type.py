from __future__ import annotations
from enum import Enum


class PermissionType(Enum):
	delegatedUserConsentable = "delegatedUserConsentable"
	delegated = "delegated"
	application = "application"

