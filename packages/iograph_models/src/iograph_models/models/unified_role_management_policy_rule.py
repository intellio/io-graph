from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(default=None,alias="target",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule":
				from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
				return UnifiedRoleManagementPolicyApprovalRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule":
				from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
				return UnifiedRoleManagementPolicyAuthenticationContextRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule":
				from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
				return UnifiedRoleManagementPolicyEnablementRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule":
				from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
				return UnifiedRoleManagementPolicyExpirationRule.model_validate(data)
			if mapping_key == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule":
				from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
				return UnifiedRoleManagementPolicyNotificationRule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

