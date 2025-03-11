from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	actionSummary: Optional[ActionSummary] = Field(alias="actionSummary",default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	identity: SerializeAsAny[Optional[AuthorizationSystemIdentity]] = Field(alias="identity",default=None,)

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
			if mapping_key == "#microsoft.graph.inactiveAwsResourceFinding":
				from .inactive_aws_resource_finding import InactiveAwsResourceFinding
				return InactiveAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAwsRoleFinding":
				from .inactive_aws_role_finding import InactiveAwsRoleFinding
				return InactiveAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAzureServicePrincipalFinding":
				from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
				return InactiveAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveGcpServiceAccountFinding":
				from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
				return InactiveGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveServerlessFunctionFinding":
				from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
				return InactiveServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveUserFinding":
				from .inactive_user_finding import InactiveUserFinding
				return InactiveUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAwsResourceFinding":
				from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
				return OverprovisionedAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAwsRoleFinding":
				from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
				return OverprovisionedAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAzureServicePrincipalFinding":
				from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
				return OverprovisionedAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedGcpServiceAccountFinding":
				from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
				return OverprovisionedGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedServerlessFunctionFinding":
				from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
				return OverprovisionedServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedUserFinding":
				from .overprovisioned_user_finding import OverprovisionedUserFinding
				return OverprovisionedUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAwsResourceFinding":
				from .super_aws_resource_finding import SuperAwsResourceFinding
				return SuperAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAwsRoleFinding":
				from .super_aws_role_finding import SuperAwsRoleFinding
				return SuperAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAzureServicePrincipalFinding":
				from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
				return SuperAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superGcpServiceAccountFinding":
				from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
				return SuperGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superServerlessFunctionFinding":
				from .super_serverless_function_finding import SuperServerlessFunctionFinding
				return SuperServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superUserFinding":
				from .super_user_finding import SuperUserFinding
				return SuperUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.unenforcedMfaAwsUserFinding":
				from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
				return UnenforcedMfaAwsUserFinding.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .action_summary import ActionSummary
from .identity_details import IdentityDetails
from .permissions_creep_index import PermissionsCreepIndex
from .authorization_system_identity import AuthorizationSystemIdentity

