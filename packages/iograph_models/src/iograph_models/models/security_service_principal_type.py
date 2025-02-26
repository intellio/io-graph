from __future__ import annotations
from enum import Enum


class SecurityServicePrincipalType(Enum):
	unknown = "unknown"
	application = "application"
	managedIdentity = "managedIdentity"
	legacy = "legacy"
	unknownFutureValue = "unknownFutureValue"

