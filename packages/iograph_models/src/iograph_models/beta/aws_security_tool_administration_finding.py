from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AwsSecurityToolAdministrationFinding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails",default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex",default=None,)
	securityTools: Optional[AwsSecurityToolWebServices | str] = Field(alias="securityTools",default=None,)
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
			if mapping_key == "#microsoft.graph.securityToolAwsResourceAdministratorFinding":
				from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
				return SecurityToolAwsResourceAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsRoleAdministratorFinding":
				from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
				return SecurityToolAwsRoleAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsServerlessFunctionAdministratorFinding":
				from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
				return SecurityToolAwsServerlessFunctionAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsUserAdministratorFinding":
				from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
				return SecurityToolAwsUserAdministratorFinding.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_details import IdentityDetails
from .permissions_creep_index import PermissionsCreepIndex
from .aws_security_tool_web_services import AwsSecurityToolWebServices
from .authorization_system_identity import AuthorizationSystemIdentity

