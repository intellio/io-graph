from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyRuleTarget(BaseModel):
	caller: Optional[str] = Field(alias="caller",default=None,)
	enforcedSettings: Optional[list[str]] = Field(alias="enforcedSettings",default=None,)
	inheritableSettings: Optional[list[str]] = Field(alias="inheritableSettings",default=None,)
	level: Optional[str] = Field(alias="level",default=None,)
	operations: Optional[str | UnifiedRoleManagementPolicyRuleTargetOperations] = Field(alias="operations",default=None,)
	targetObjects: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="targetObjects",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .unified_role_management_policy_rule_target_operations import UnifiedRoleManagementPolicyRuleTargetOperations
from .directory_object import DirectoryObject

