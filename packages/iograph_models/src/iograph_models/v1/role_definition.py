from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class RoleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	rolePermissions: Optional[list[RolePermission]] = Field(alias="rolePermissions", default=None,)
	roleAssignments: Optional[list[Annotated[Union[DeviceAndAppManagementRoleAssignment],Field(discriminator="odata_type")]]] = Field(alias="roleAssignments", default=None,)

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
			if mapping_key == "#microsoft.graph.deviceAndAppManagementRoleDefinition":
				from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
				return DeviceAndAppManagementRoleDefinition.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .role_permission import RolePermission
from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment

