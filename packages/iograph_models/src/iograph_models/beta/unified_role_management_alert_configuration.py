from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlertConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alertDefinitionId: Optional[str] = Field(alias="alertDefinitionId",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	scopeId: Optional[str] = Field(alias="scopeId",default=None,)
	scopeType: Optional[str] = Field(alias="scopeType",default=None,)
	alertDefinition: Optional[UnifiedRoleManagementAlertDefinition] = Field(alias="alertDefinition",default=None,)

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
			if mapping_key == "#microsoft.graph.invalidLicenseAlertConfiguration":
				from .invalid_license_alert_configuration import InvalidLicenseAlertConfiguration
				return InvalidLicenseAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.noMfaOnRoleActivationAlertConfiguration":
				from .no_mfa_on_role_activation_alert_configuration import NoMfaOnRoleActivationAlertConfiguration
				return NoMfaOnRoleActivationAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.redundantAssignmentAlertConfiguration":
				from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration
				return RedundantAssignmentAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration":
				from .roles_assigned_outside_privileged_identity_management_alert_configuration import RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration
				return RolesAssignedOutsidePrivilegedIdentityManagementAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.sequentialActivationRenewalsAlertConfiguration":
				from .sequential_activation_renewals_alert_configuration import SequentialActivationRenewalsAlertConfiguration
				return SequentialActivationRenewalsAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.staleSignInAlertConfiguration":
				from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration
				return StaleSignInAlertConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration":
				from .too_many_global_admins_assigned_to_tenant_alert_configuration import TooManyGlobalAdminsAssignedToTenantAlertConfiguration
				return TooManyGlobalAdminsAssignedToTenantAlertConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .unified_role_management_alert_definition import UnifiedRoleManagementAlertDefinition

