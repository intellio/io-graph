from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegeEscalationFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	identity: SerializeAsAny[Optional[AuthorizationSystemIdentity]] = Field(alias="identity",default=None,)
	privilegeEscalationDetails: Optional[list[PrivilegeEscalation]] = Field(alias="privilegeEscalationDetails",default=None,)

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
			if mapping_key == "#microsoft.graph.privilegeEscalationAwsResourceFinding":
				from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
				return PrivilegeEscalationAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationAwsRoleFinding":
				from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
				return PrivilegeEscalationAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationGcpServiceAccountFinding":
				from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
				return PrivilegeEscalationGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationUserFinding":
				from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
				return PrivilegeEscalationUserFinding.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_details import IdentityDetails
from .permissions_creep_index import PermissionsCreepIndex
from .authorization_system_identity import AuthorizationSystemIdentity
from .privilege_escalation import PrivilegeEscalation

