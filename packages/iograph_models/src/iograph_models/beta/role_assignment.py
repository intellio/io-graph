from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class RoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resourceScopes: Optional[list[str]] = Field(alias="resourceScopes", default=None,)
	scopeMembers: Optional[list[str]] = Field(alias="scopeMembers", default=None,)
	scopeType: Optional[RoleAssignmentScopeType | str] = Field(alias="scopeType", default=None,)
	roleDefinition: Optional[Union[DeviceAndAppManagementRoleDefinition]] = Field(alias="roleDefinition", default=None,discriminator="odata_type", )

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

from .role_assignment_scope_type import RoleAssignmentScopeType
from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
