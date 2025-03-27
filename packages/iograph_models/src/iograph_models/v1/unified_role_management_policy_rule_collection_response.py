from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[UnifiedRoleManagementPolicyApprovalRule, UnifiedRoleManagementPolicyAuthenticationContextRule, UnifiedRoleManagementPolicyEnablementRule, UnifiedRoleManagementPolicyExpirationRule, UnifiedRoleManagementPolicyNotificationRule]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule

