from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyNotificationRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(default=None,alias="target",)
	isDefaultRecipientsEnabled: Optional[bool] = Field(default=None,alias="isDefaultRecipientsEnabled",)
	notificationLevel: Optional[str] = Field(default=None,alias="notificationLevel",)
	notificationRecipients: Optional[list[str]] = Field(default=None,alias="notificationRecipients",)
	notificationType: Optional[str] = Field(default=None,alias="notificationType",)
	recipientType: Optional[str] = Field(default=None,alias="recipientType",)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

