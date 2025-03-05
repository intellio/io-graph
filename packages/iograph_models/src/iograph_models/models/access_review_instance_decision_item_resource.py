from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemResource(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource":
				from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
				return AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource":
				from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource
				return AccessReviewInstanceDecisionItemAzureRoleResource.model_validate(data)
			if mapping_key == "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource":
				from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource
				return AccessReviewInstanceDecisionItemServicePrincipalResource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


