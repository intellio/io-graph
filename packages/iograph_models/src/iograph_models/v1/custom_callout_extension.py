from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class CustomCalloutExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authenticationConfiguration: Optional[Union[AzureAdPopTokenAuthentication, AzureAdTokenAuthentication]] = Field(alias="authenticationConfiguration", default=None,discriminator="odata_type", )
	clientConfiguration: Optional[CustomExtensionClientConfiguration] = Field(alias="clientConfiguration", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endpointConfiguration: Optional[Union[HttpRequestEndpoint, LogicAppTriggerEndpointConfiguration]] = Field(alias="endpointConfiguration", default=None,discriminator="odata_type", )

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

from .azure_ad_pop_token_authentication import AzureAdPopTokenAuthentication
from .azure_ad_token_authentication import AzureAdTokenAuthentication
from .custom_extension_client_configuration import CustomExtensionClientConfiguration
from .http_request_endpoint import HttpRequestEndpoint
from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration

