from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyRuleTarget(BaseModel):
	caller: Optional[str] = Field(default=None,alias="caller",)
	enforcedSettings: Optional[list[str]] = Field(default=None,alias="enforcedSettings",)
	inheritableSettings: Optional[list[str]] = Field(default=None,alias="inheritableSettings",)
	level: Optional[str] = Field(default=None,alias="level",)
	operations: Optional[UnifiedRoleManagementPolicyRuleTargetOperations] = Field(default=None,alias="operations",)
	targetObjects: Optional[list[DirectoryObject]] = Field(default=None,alias="targetObjects",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .unified_role_management_policy_rule_target_operations import UnifiedRoleManagementPolicyRuleTargetOperations
from .directory_object import DirectoryObject

