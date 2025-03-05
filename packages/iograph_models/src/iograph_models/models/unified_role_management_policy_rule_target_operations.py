from __future__ import annotations
from enum import StrEnum


class UnifiedRoleManagementPolicyRuleTargetOperations(StrEnum):
	all = "all"
	activate = "activate"
	deactivate = "deactivate"
	assign = "assign"
	update = "update"
	remove = "remove"
	extend = "extend"
	renew = "renew"
	unknownFutureValue = "unknownFutureValue"

