from __future__ import annotations
from enum import Enum


class AuthenticationMethodsPolicyMigrationState(Enum):
	preMigration = "preMigration"
	migrationInProgress = "migrationInProgress"
	migrationComplete = "migrationComplete"
	unknownFutureValue = "unknownFutureValue"

