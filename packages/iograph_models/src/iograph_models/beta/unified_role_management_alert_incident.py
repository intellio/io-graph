from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.invalidLicenseAlertIncident":
				from .invalid_license_alert_incident import InvalidLicenseAlertIncident
				return InvalidLicenseAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.noMfaOnRoleActivationAlertIncident":
				from .no_mfa_on_role_activation_alert_incident import NoMfaOnRoleActivationAlertIncident
				return NoMfaOnRoleActivationAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.redundantAssignmentAlertIncident":
				from .redundant_assignment_alert_incident import RedundantAssignmentAlertIncident
				return RedundantAssignmentAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident":
				from .roles_assigned_outside_privileged_identity_management_alert_incident import RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident
				return RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.sequentialActivationRenewalsAlertIncident":
				from .sequential_activation_renewals_alert_incident import SequentialActivationRenewalsAlertIncident
				return SequentialActivationRenewalsAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.staleSignInAlertIncident":
				from .stale_sign_in_alert_incident import StaleSignInAlertIncident
				return StaleSignInAlertIncident.model_validate(data)
			if mapping_key == "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertIncident":
				from .too_many_global_admins_assigned_to_tenant_alert_incident import TooManyGlobalAdminsAssignedToTenantAlertIncident
				return TooManyGlobalAdminsAssignedToTenantAlertIncident.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


