from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ManagedTenantsManagedTenantOperationError(BaseModel):
	error: Optional[str] = Field(alias="error", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantExecutionError":
				from .managed_tenants_managed_tenant_execution_error import ManagedTenantsManagedTenantExecutionError
				return ManagedTenantsManagedTenantExecutionError.model_validate(data)
			if mapping_key == "#microsoft.graph.managedTenants.managedTenantGenericError":
				from .managed_tenants_managed_tenant_generic_error import ManagedTenantsManagedTenantGenericError
				return ManagedTenantsManagedTenantGenericError.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

