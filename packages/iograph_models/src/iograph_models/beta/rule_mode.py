from __future__ import annotations
from enum import StrEnum


class RuleMode(StrEnum):
	audit = "audit"
	auditAndNotify = "auditAndNotify"
	enforce = "enforce"
	pendingDeletion = "pendingDeletion"
	test = "test"

