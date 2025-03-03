from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class RoleAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	resourceScopes: Optional[list[str]] = Field(default=None,alias="resourceScopes",)
	roleDefinition: Optional[RoleDefinition] = Field(default=None,alias="roleDefinition",)

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
			if mapping_key == "#microsoft.graph.deviceAndAppManagementRoleAssignment":
				from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
				return DeviceAndAppManagementRoleAssignment.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .role_definition import RoleDefinition

