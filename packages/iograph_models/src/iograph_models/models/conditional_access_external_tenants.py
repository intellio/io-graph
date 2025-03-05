from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessExternalTenants(BaseModel):
	membershipKind: Optional[ConditionalAccessExternalTenantsMembershipKind] = Field(default=None,alias="membershipKind",)
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
			if mapping_key == "#microsoft.graph.conditionalAccessAllExternalTenants":
				from .conditional_access_all_external_tenants import ConditionalAccessAllExternalTenants
				return ConditionalAccessAllExternalTenants.model_validate(data)
			if mapping_key == "#microsoft.graph.conditionalAccessEnumeratedExternalTenants":
				from .conditional_access_enumerated_external_tenants import ConditionalAccessEnumeratedExternalTenants
				return ConditionalAccessEnumeratedExternalTenants.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

