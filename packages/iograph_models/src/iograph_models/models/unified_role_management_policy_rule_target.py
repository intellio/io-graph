from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyRuleTarget(BaseModel):
	caller: Optional[str] = Field(default=None,alias="caller",)
	enforcedSettings: list[Optional[str]] = Field(alias="enforcedSettings",)
	inheritableSettings: list[Optional[str]] = Field(alias="inheritableSettings",)
	level: Optional[str] = Field(default=None,alias="level",)
	operations: Optional[UnifiedRoleManagementPolicyRuleTargetOperations] = Field(default=None,alias="operations",)
	targetObjects: list[DirectoryObject] = Field(alias="targetObjects",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .unified_role_management_policy_rule_target_operations import UnifiedRoleManagementPolicyRuleTargetOperations
from .directory_object import DirectoryObject

