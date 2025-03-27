from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyNotificationRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementPolicyNotificationRule"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleManagementPolicyNotificationRule")
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(alias="target", default=None,)
	isDefaultRecipientsEnabled: Optional[bool] = Field(alias="isDefaultRecipientsEnabled", default=None,)
	notificationLevel: Optional[str] = Field(alias="notificationLevel", default=None,)
	notificationRecipients: Optional[list[str]] = Field(alias="notificationRecipients", default=None,)
	notificationType: Optional[str] = Field(alias="notificationType", default=None,)
	recipientType: Optional[str] = Field(alias="recipientType", default=None,)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

