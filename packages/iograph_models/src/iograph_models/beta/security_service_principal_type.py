from __future__ import annotations
from enum import StrEnum


class SecurityServicePrincipalType(StrEnum):
	unknown = "unknown"
	application = "application"
	managedIdentity = "managedIdentity"
	legacy = "legacy"
	unknownFutureValue = "unknownFutureValue"

