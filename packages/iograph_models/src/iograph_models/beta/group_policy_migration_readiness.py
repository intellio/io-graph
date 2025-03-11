from __future__ import annotations
from enum import StrEnum


class GroupPolicyMigrationReadiness(StrEnum):
	none = "none"
	partial = "partial"
	complete = "complete"
	error = "error"
	notApplicable = "notApplicable"

