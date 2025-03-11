from __future__ import annotations
from enum import StrEnum


class AuthenticationMethodsPolicyMigrationState(StrEnum):
	preMigration = "preMigration"
	migrationInProgress = "migrationInProgress"
	migrationComplete = "migrationComplete"
	unknownFutureValue = "unknownFutureValue"

