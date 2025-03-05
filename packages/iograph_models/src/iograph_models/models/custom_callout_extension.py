from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class CustomCalloutExtension(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	authenticationConfiguration: SerializeAsAny[Optional[CustomExtensionAuthenticationConfiguration]] = Field(default=None,alias="authenticationConfiguration",)
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(default=None,alias="clientConfiguration",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endpointConfiguration: SerializeAsAny[Optional[CustomExtensionEndpointConfiguration]] = Field(default=None,alias="endpointConfiguration",)

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
			if mapping_key == "#microsoft.graph.accessPackageAssignmentRequestWorkflowExtension":
				from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
				return AccessPackageAssignmentRequestWorkflowExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.accessPackageAssignmentWorkflowExtension":
				from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
				return AccessPackageAssignmentWorkflowExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.customAuthenticationExtension":
				from .custom_authentication_extension import CustomAuthenticationExtension
				return CustomAuthenticationExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.onTokenIssuanceStartCustomExtension":
				from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
				return OnTokenIssuanceStartCustomExtension.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.customTaskExtension":
				from .identity_governance_custom_task_extension import IdentityGovernanceCustomTaskExtension
				return IdentityGovernanceCustomTaskExtension.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

