from __future__ import annotations
from enum import StrEnum


class PermissionsDefinitionIdentityType(StrEnum):
	user = "user"
	role = "role"
	application = "application"
	managedIdentity = "managedIdentity"
	serviceAccount = "serviceAccount"
	unknownFutureValue = "unknownFutureValue"

