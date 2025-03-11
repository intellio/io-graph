from __future__ import annotations
from enum import StrEnum


class PlannerRelationshipUserRoles(StrEnum):
	defaultRules = "defaultRules"
	groupOwners = "groupOwners"
	groupMembers = "groupMembers"
	taskAssignees = "taskAssignees"
	applications = "applications"
	unknownFutureValue = "unknownFutureValue"

